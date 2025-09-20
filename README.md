# Data Scientist GenAI Agent - Prefeitura do Rio

## Descrição

Este projeto implementa um agente autônomo com IA Generativa capaz de responder perguntas em linguagem natural sobre dados públicos do Rio de Janeiro, usando BigQuery, LangGraph e LLMs.

## Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure variáveis de ambiente:
   - `OPENAI_API_KEY`: sua chave OpenAI.
   - `BIGQUERY_CREDENTIALS_PATH`: caminho para o JSON de credenciais do BigQuery.

3. Execute o agente:
   ```bash
   python main.py
   ```

## Estrutura

- `agent/agent.py`: arquitetura do agente e orquestração do LangGraph.
- `agent/sql_generator.py`: geração e validação de queries SQL.
- `agent/bigquery_client.py`: integração BigQuery.
- `agent/memory.py`: memória e contexto do agente.
- `tests/`: (opcional) testes unitários.
- `requisitos_do_agente.md`: critérios do desafio.

## Diferenciais

- Validação de SQL antes da execução.
- Tratamento de erros e perguntas ambíguas.
- Memória de interações.
- Código modular e documentado.

## Referências

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://python.langchain.com/)
- [BigQuery Python Client](https://cloud.google.com/bigquery/docs/reference/libraries)
