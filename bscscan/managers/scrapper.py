import requests

from django.conf import settings


class Scrapper:
    paylaod = {"module": "account", "sort": "asc"}
    actions = ["txlist", "txlistinternal", "tokentx", "tokennfttx"]

    def scrap_data(self, payload: dict) -> list:
        copied_payload = payload.copy()
        copied_payload.update({"apikey": settings.BSCSCAN_API_KEY})

        results = requests.get(settings.BSCSCAN_URL, params=copied_payload)

        return results.json()["result"]

    def scrap_transaction(self, payload: dict) -> dict:
        results_dict = {}
        copied_payload = payload.copy()

        for action in self.actions:
            copied_payload.update(self.paylaod)
            copied_payload.update({"action": action})
            results_dict.update({action: self.scrap_data(copied_payload)})

        return results_dict
