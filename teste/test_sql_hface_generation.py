
from agent.sql_generator_hface import generate_sql_hface

import re

def extrai_sql_puro(texto):
    match = re.search(r"(SELECT[\s\S]+?;)", texto, re.IGNORECASE)
    return match.group(1) if match else texto

def test_sql_generation():
    perguntas = [
        "Quantos chamados foram abertos no bairro Copacabana em 2023?"
    ]
    for pergunta in perguntas:
        resposta = generate_sql_hface(pergunta)
        sql_puro = extrai_sql_puro(resposta)
        print(sql_puro)

if __name__ == "__main__":
    test_sql_generation()
