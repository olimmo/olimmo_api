import requests
from decouple import config


class LobstrPropertyFetcher:
    def __init__(self, run_id):
        self.run_id = run_id

    def get_properties(self):
        if not self.run_id:
            return

        headers = {
            "Authorization": f'Token {config("LOBSTR_API_KEY")}',
            "Content-Type": "application/json",
        }
        res = requests.get(
            f"https://api.lobstr.io/v1/results?run={self.run_id}", headers=headers
        )

        if res.status_code == 200:
            return res.json()["data"]
