import re

def generate_sql(question, llm):
    prompt = f"Gere uma consulta SQL para responder: '{question}'. Use as tabelas datario.adm_central_atendimento_1746.chamado e datario.dados_mestres.bairro."
    response = llm(prompt)
    return response.strip()

def validate_sql(sql):
    # Exemplo simples para evitar DELETE, UPDATE, DROP, etc.
    forbidden = re.compile(r"\b(DELETE|UPDATE|DROP|INSERT|ALTER)\b", re.IGNORECASE)
    if forbidden.search(sql):
        return False, "Comando perigoso detectado."
    if not sql.lower().startswith("select"):
        return False, "Apenas consultas SELECT são permitidas."
    # Poderia adicionar validação de custo/partições/etc.
    return True, ""
