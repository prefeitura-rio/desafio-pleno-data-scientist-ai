from google.cloud import bigquery

class BigQueryClient:
    def __init__(self, credentials_path):
        self.client = bigquery.Client.from_service_account_json(credentials_path)

    def run_query(self, sql):
        query_job = self.client.query(sql)
        results = query_job.result()
        return [dict(row.items()) for row in results]
