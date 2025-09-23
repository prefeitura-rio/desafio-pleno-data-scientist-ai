import re
import openai


def generate_sql(question, llm):
    prompt = f"Gere uma consulta SQL para responder: '{question}'. Use as tabelas datario.adm_central_atendimento_1746.chamado e datario.dados_mestres.bairro."
    client = openai.OpenAI(api_key=llm.api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


def validate_sql(sql):
    # Exemplo simples para evitar DELETE, UPDATE, DROP, etc.
    forbidden = re.compile(r"\b(DELETE|UPDATE|DROP|INSERT|ALTER)\b", re.IGNORECASE)
    if forbidden.search(sql):
        return False, "Comando perigoso detectado."
    if not sql.lower().startswith("select"):
        return False, "Apenas consultas SELECT são permitidas."
    return True, ""
