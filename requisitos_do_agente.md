# Requisitos do Agente

- Receber perguntas em linguagem natural.
- Gerar uma query SQL eficiente baseada na pergunta.
- Validar a query antes de executar (segurança, custo, sintaxe).
- Executar a consulta no BigQuery sobre as tabelas:
  - datario.adm_central_atendimento_1746.chamado (particionada por data_particao)
  - datario.dados_mestres.bairro
- Enriquecer a resposta em linguagem natural e clara.
- Tratar perguntas ambíguas solicitando esclarecimento ao usuário.
- Lidar com erros de execução ou resultados inesperados.
- Documentar o código e o uso do agente.
- (Diferencial) Implementar memória/contexto.

## Fluxo Sugerido

1. Usuário faz pergunta.
2. Agente gera SQL.
3. SQL é validada.
4. Consulta é executada.
5. Resultados são interpretados e apresentados.
6. Se erro/ambiguidade, solicita esclarecimento ou apresenta mensagem adequada.
