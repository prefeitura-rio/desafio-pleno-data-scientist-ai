import openai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("OPENAI_API_KEY não encontrado nas variáveis de ambiente.")
else:
    try:
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Diga 'Olá, OpenAI!'"}]
        )
        print("Conexão bem-sucedida! Resposta:", response.choices[0].message.content)
    except Exception as e:
        print("Erro ao conectar ao OpenAI:", e)
