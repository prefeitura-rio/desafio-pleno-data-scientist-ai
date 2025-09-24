from langgraph.graph import StateGraph


class AgentState(dict):
    pass


graph = StateGraph(AgentState)
graph.add_node("input", lambda s: s)
graph.add_node("output", lambda s: s)
graph.add_edge("START", "input")
graph.add_edge("input", "output")
app = graph.compile()
print("Graph compiled OK!")
