# Copilot Instructions for Data Scientist GenAI Agent

## Project Overview
This repository implements an autonomous GenAI agent for answering natural language questions about public data from Rio de Janeiro, leveraging BigQuery, LangGraph, and LLMs.

## Architecture & Key Components
- `main.py`: Entry point. Loads environment variables and starts the agent.
- `agent/agent.py`: Orchestrates the agent logic and LangGraph workflow.
- `agent/sql_generator.py`: Generates and validates SQL queries from user questions.
- `agent/bigquery_client.py`: Handles BigQuery integration and query execution.
- `agent/memory.py`: Manages agent memory and conversational context.
- `tests/`: Contains unit tests (optional).
- `requisitos_do_agente.md`: Challenge requirements and acceptance criteria.

## Developer Workflows
- **Install dependencies:** `pip install -r requirements.txt`
- **Run agent:** `python main.py`
- **Environment variables required:**
  - `OPENAI_API_KEY` (OpenAI access)
  - `BIGQUERY_CREDENTIALS_PATH` (path to BigQuery credentials JSON)
- **Testing:** Place tests in `tests/` and run with `pytest`.

## Patterns & Conventions
- SQL queries are always validated before execution for security, cost, and syntax.
- Error handling and ambiguity resolution are core: agent requests clarification for unclear questions and provides informative error messages.
- Memory of previous interactions is maintained for context-aware responses.
- Modular code: Each major function is separated into its own file for clarity and maintainability.
- All code and agent flows should be documented and easy to follow.

## Integration Points
- **BigQuery:** Queries run against:
  - `datario.adm_central_atendimento_1746.chamado` (partitioned by `data_particao`)
  - `datario.dados_mestres.bairro`
- **LangGraph:** Used for agent orchestration and workflow management.
- **LLMs:** Used for natural language understanding and response generation.

## Examples
- To add a new data source, extend `bigquery_client.py` and update SQL generation logic in `sql_generator.py`.
- To customize agent memory, modify `memory.py`.
- For new workflows, update orchestration in `agent.py`.

## References
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://python.langchain.com/)
- [BigQuery Python Client](https://cloud.google.com/bigquery/docs/reference/libraries)

---
**Feedback:** If any section is unclear or missing, please specify so it can be improved for future AI agents.
