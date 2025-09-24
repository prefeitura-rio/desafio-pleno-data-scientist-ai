class AgentMemory:
    def __init__(self):
        self.history = []

    def add_interaction(self, question):
        self.history.append({"question": question})

    def update(self, question, sql_query, result):
        self.history.append(
            {"question": question, "sql_query": sql_query, "result": result}
        )

    def get_last(self):
        return self.history[-1] if self.history else None

    def clear(self):
        self.history = []
