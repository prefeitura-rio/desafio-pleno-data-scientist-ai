from agent.sql_generator_hface import generate_sql_hface
from agent.bigquery_client import BigQueryClient
from agent.memory import AgentMemory


def run_agent_hface(huggingface_api_key, bigquery_credentials_path):
    memory = AgentMemory()
    bigquery_client = BigQueryClient(bigquery_credentials_path)

    print(
        "Agente GenAI (Hugging Face) iniciado. Pergunte sobre dados públicos do Rio de Janeiro."
    )
    while True:
        user_input = input("Usuário: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Encerrando agente.")
            break
        # Gera SQL usando Hugging Face
        sql_query = generate_sql_hface(user_input)
        # Validação básica do SQL
        if (
            not sql_query
            or sql_query.strip().lower().startswith("erro")
            or not sql_query.strip().lower().startswith("select")
        ):
            print(
                f"Não foi possível gerar uma consulta SQL válida. Resposta do modelo: {sql_query}"
            )
            memory.update(user_input, sql_query, None)
            continue
        # Pós-processamento: substitui colchetes por crases
        sql_query_bq = sql_query.replace("[", "`").replace("]", "`")
        # Executa consulta no BigQuery
        try:
            result = bigquery_client.run_query(sql_query_bq)
            print("Resultado:", result)
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")
            result = None
        memory.update(user_input, sql_query_bq, result)
