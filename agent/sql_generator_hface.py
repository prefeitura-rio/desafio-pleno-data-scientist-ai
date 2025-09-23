import os
import requests
from dotenv import load_dotenv
load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
MODEL = "gpt2"  # Ou outro modelo disponível

# Função para gerar SQL usando Hugging Face

def generate_sql_hface(question):
    prompt = f"Gere uma consulta SQL para responder: '{question}'. Use as tabelas datario.adm_central_atendimento_1746.chamado e datario.dados_mestres.bairro."
    url = f"https://api-inference.huggingface.co/models/{MODEL}"
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {"inputs": prompt}
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result[0]["generated_text"] if isinstance(result, list) and "generated_text" in result[0] else str(result)
    except Exception as e:
        return f"Erro ao conectar ao Hugging Face API: {e}"

# Função de validação igual à anterior

def validate_sql_hface(sql):
    import re
    if re.search(r"drop|delete|update|insert|alter|create", sql, re.IGNORECASE):
        return False, "Comando perigoso detectado."
    if not sql.lower().startswith("select"):
        return False, "Apenas consultas SELECT são permitidas."
    return True, ""
