from google.cloud import bigquery
from dotenv import load_dotenv

load_dotenv()
client = bigquery.Client()
dataset = client.get_dataset("datario.dados_mestres")
print(dataset.location)
