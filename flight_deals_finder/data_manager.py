import requests


class DataManager:
    """This class is responsible for talking to the Google Sheet."""

    def __init__(self, endpoint, username, password):
        self.endpoint = endpoint
        self.auth = (username, password)

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
