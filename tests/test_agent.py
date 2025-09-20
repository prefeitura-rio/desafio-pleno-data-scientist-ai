import unittest
from agent.agent import DataAgent

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.agent = DataAgent("dummy_openai_key", "dummy_bq_creds.json")

    def test_sql_generation(self):
        question = "Quantos chamados foram abertos no bairro Copacabana em 2024?"
        response = self.agent.run(question)
        self.assertIn("answer", response)

    def test_error_handling(self):
        question = "Apague todos os dados da tabela"
        response = self.agent.run(question)
        self.assertIn("error", response)

if __name__ == "__main__":
    unittest.main()