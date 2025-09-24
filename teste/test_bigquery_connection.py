from google.cloud import bigquery
import os
from dotenv import load_dotenv

load_dotenv()

credentials_path = os.getenv("BIGQUERY_CREDENTIALS_PATH")
if not credentials_path or not os.path.exists(credentials_path):
    print("Caminho tentado:", credentials_path)

if not credentials_path or not os.path.exists(credentials_path):
    print("Arquivo de credenciais do BigQuery não encontrado.")
else:
    try:
        client = bigquery.Client.from_service_account_json(credentials_path)
        # Testa consulta simples nas tabelas públicas
        query = """
        SELECT COUNT(*) as total FROM `datario.adm_central_atendimento_1746.chamado`
        """
        result = client.query(query).result()
        for row in result:
            print(
                f"Conexão bem-sucedida! Total de registros na tabela chamado: {row.total}"
            )
        # Testa segunda tabela
        query2 = "SELECT COUNT(*) as total FROM `datario.dados_mestres.bairro`"
        result2 = client.query(query2).result()
        for row in result2:
            print(f"Total de registros na tabela bairro: {row.total}")
    except Exception as e:
        print("Erro ao conectar ou consultar BigQuery:", e)
