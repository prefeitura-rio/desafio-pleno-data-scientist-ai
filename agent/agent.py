import os
from openai import OpenAI
from langgraph.graph import StateGraph, START
from agent.sql_generator import generate_sql, validate_sql
from agent.bigquery_client import BigQueryClient
from agent.memory import AgentMemory
from typing import TypedDict


class AgentState(TypedDict):
    user_input: str
    generated_sql: str
    validated_sql: str
    query_result: str
    response: str
    error: str


class DataAgent:
    def __init__(self, llm_api_key, bq_credentials_path):
        self.llm = OpenAI(api_key=llm_api_key)
        self.memory = AgentMemory()
        self.bq_client = BigQueryClient(bq_credentials_path)
        self.graph = self._build_graph()
        self.app = self.graph.compile()

    def _build_graph(self):
        graph = StateGraph(AgentState)
        graph.add_node("input", self._input_handler)
        graph.add_node("sql_generation", self._sql_generation_handler)
        graph.add_node("sql_validation", self._sql_validation_handler)
        graph.add_node("query_execution", self._query_execution_handler)
        graph.add_node("response_generation", self._response_generation_handler)
        graph.add_node("error", self._error_handler)
        graph.add_edge(START, "input")
        graph.add_edge("input", "sql_generation")
        graph.add_edge("sql_generation", "sql_validation")
        graph.add_edge("sql_validation", "query_execution")
        graph.add_edge("query_execution", "response_generation")
        graph.add_edge("sql_validation", "error")
        graph.add_edge("query_execution", "error")
        return graph

    def run(self, question):
        state = {"user_input": question, "memory": self.memory}
        return self.app.invoke(state)

    def _input_handler(self, state):
        self.memory.add_interaction(state["user_input"])
        return state

    def _sql_generation_handler(self, state):
        sql = generate_sql(state["user_input"], self.llm)
        state["sql"] = sql
        return state

    def _sql_validation_handler(self, state):
        valid, reason = validate_sql(state["sql"])
        if not valid:
            state["error"] = f"SQL inválido: {reason}"
            return "error"
        return state

    def _query_execution_handler(self, state):
        try:
            results = self.bq_client.run_query(state["sql"])
            state["results"] = results
            return state
        except Exception as e:
            state["error"] = str(e)
            return "error"

    def _response_generation_handler(self, state):
        answer = self.llm(
            f"Explique os resultados para a pergunta: '{state['user_input']}' usando: {state['results']}"
        )
        state["answer"] = answer
        return state

    def _error_handler(self, state):
        return {"error": state.get("error", "Erro desconhecido")}
