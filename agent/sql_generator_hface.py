
import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
MODEL = "HuggingFaceH4/zephyr-7b-beta:featherless-ai"
API_URL = "https://api-inference.huggingface.co/models/Chat2DB/Chat2DB-SQL-7B"

#API_URL = "https://router.huggingface.co/v1/chat/completions"

def generate_sql_hface(question):
    try:
        headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
        prompt = (
            f"Responda apenas com o código SQL, sem explicações, para: '{question}'. "
            "Use o dataset datario.adm_central_atendimento_1746.chamado "
            "e o dataset datario.dados_mestres.bairro. "
            "Gere o código SQL mais simples possível, sem subconsultas ou estruturas complexas."
        )
        payload = {
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "model": MODEL
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        texto = result["choices"][0]["message"]["content"] if "choices" in result and result["choices"] else str(result)
        import re
        match = re.search(r"(SELECT[\s\S]+?;)", texto, re.IGNORECASE)
        sql = match.group(1) if match else texto
        def replace_column_quotes(sql):
            linhas = sql.splitlines()
            novas_linhas = []
            for linha in linhas:
                if linha.strip().upper().startswith(('SELECT', 'FROM', 'JOIN')):
                    novas_linhas.append(re.sub(r"'([^']+)'", r"`\1`", linha))
                else:
                    novas_linhas.append(linha)
            return '\n'.join(novas_linhas)
        sql_corrigido = replace_column_quotes(sql)
        sql_ascii = ''.join(c for c in sql_corrigido if ord(c) < 128)
        # Validação do SQL
        is_valid, msg = validate_sql_hface(sql_ascii)
        if not is_valid:
            return f"SQL inválido gerado pelo modelo: {msg}\n{sql_ascii}"
        return sql_ascii
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
