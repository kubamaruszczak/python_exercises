import requests
import os


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self):
        self.endpoint = "https://api.sheety.co/a042454111d46a1f9daaa68e9f7ca593/flightDealsFinder/prices"
        self.auth = (os.environ.get("USERNAME"), os.environ.get("PASSWORD"))

    def get_sheet(self):
        response = requests.get(url=self.endpoint, auth=self.auth)
        response.raise_for_status()
        return response.json()["prices"]

    def update_row(self, row_data):
        body = {
            "price": row_data,
        }
        response = requests.put(url=f"{self.endpoint}/{row_data['id']}", json=body, auth=self.auth)
        response.raise_for_status()
