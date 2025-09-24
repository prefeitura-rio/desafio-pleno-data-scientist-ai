import requests
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
model = "BAAI/bge-base-en-v1.5"  # Modelo usado para feature extraction
hf_token = os.getenv("HF_API_TOKEN")
if not hf_token:
    print("HF_API_TOKEN não encontrado nas variáveis de ambiente.")
else:
    try:
        client = InferenceClient(
            provider="hf-inference",
            api_key=hf_token,
        )
        result = client.feature_extraction(
            "The model is BAAI.",
            model="BAAI/bge-base-en-v1.5",
        )
        print("Conexão bem-sucedida! Resultado da extração de features:", result)

    except Exception as e:
        print("Erro ao conectar ao Hugging Face API:", e)
