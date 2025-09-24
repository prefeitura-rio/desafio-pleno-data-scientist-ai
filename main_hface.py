import os
from agent.agent_hface import run_agent_hface


def main():
    # Carrega variáveis de ambiente
    openai_api_key = os.getenv("OPENAI_API_KEY")
    bigquery_credentials_path = os.getenv("BIGQUERY_CREDENTIALS_PATH")
    huggingface_api_key = os.getenv("HF_API_TOKEN")

    if not huggingface_api_key:
        raise EnvironmentError("HF_API_TOKEN não definido.")
    if not bigquery_credentials_path:
        raise EnvironmentError("BIGQUERY_CREDENTIALS_PATH não definido.")

    # Executa o agente usando Hugging Face
    run_agent_hface(
        huggingface_api_key=huggingface_api_key,
        bigquery_credentials_path=bigquery_credentials_path,
    )


if __name__ == "__main__":
    main()
