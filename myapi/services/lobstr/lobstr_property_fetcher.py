import os

import requests
import json
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
        # to remove
        else:
            return self._get_sample_data()

    def _get_sample_data(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(
            current_dir, "..", "..", "..", "tmp", "lobstr_leboncoin_sample_data.json"
        )

        with open(file_path, "r") as json_file:
            data = json.load(json_file)

            return data
