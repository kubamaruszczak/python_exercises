import requests
import os

PRICES_ENDPOINT = "https://api.sheety.co/a042454111d46a1f9daaa68e9f7ca593/flightDealsFinder/prices"
USERS_ENDPOINT = "https://api.sheety.co/a042454111d46a1f9daaa68e9f7ca593/flightDealsFinder/users"


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self):
        self.auth = (os.environ.get("USERNAME"), os.environ.get("PASSWORD"))

    def get_sheet(self):
        response = requests.get(url=PRICES_ENDPOINT, auth=self.auth)
        response.raise_for_status()
        return response.json()["prices"]

    def update_row(self, row_data):
        body = {
            "price": row_data,
        }
        response = requests.put(url=f"{PRICES_ENDPOINT}/{row_data['id']}", json=body, auth=self.auth)
        response.raise_for_status()

    def get_emails(self):
        response = requests.get(url=USERS_ENDPOINT, auth=self.auth)
        response.raise_for_status()
        emails = [person_dict["email"] for person_dict in response.json()["users"]]
        return emails
