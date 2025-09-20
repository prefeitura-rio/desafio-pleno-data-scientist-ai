import os
from agent.agent import DataAgent
from dotenv import load_dotenv
import os

load_dotenv()  # Isso carrega as variáveis do .env

llm_api_key = os.getenv("OPENAI_API_KEY")
bq_credentials_path = os.getenv("BIGQUERY_CREDENTIALS_PATH")

def main():
    llm_api_key = os.getenv("OPENAI_API_KEY")
    bq_credentials_path = os.getenv("BIGQUERY_CREDENTIALS_PATH")
    agent = DataAgent(llm_api_key, bq_credentials_path)

    print("Pergunte ao agente (digite 'sair' para encerrar):")
    while True:
        question = input("> ")
        if question.lower() == "sair":
            break
        response = agent.run(question)
        print("Resposta:", response.get("answer", response.get("error", "Erro desconhecido")))

if __name__ == "__main__":
    main()
