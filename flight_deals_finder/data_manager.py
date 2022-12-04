import requests


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self, endpoint, username, password):
        self.endpoint = endpoint
        self.auth = (username, password)
        self.sheet_data = []

    def get_sheet(self):
        response = requests.get(url=self.endpoint, auth=self.auth)
        response.raise_for_status()
        self.sheet_data = response.json()["prices"]
        for row in self.sheet_data:
            if row["iataCode"] == "":
                row["iataCode"] = "TEST"

    def update_sheet(self):
        for row in self.sheet_data:
            body = {
                "price": row,
            }
            response = requests.put(url=f"{self.endpoint}/{row['id']}", json=body, auth=self.auth)
            print(response.text)
            response.raise_for_status()
