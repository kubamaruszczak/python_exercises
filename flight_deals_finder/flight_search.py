import requests


class FlightSearch:
    """Class responsible for talking with Flight Search API"""

    def __init__(self, api_key):
        self.endpoint = "https://api.tequila.kiwi.com"
        self.header = {"apikey": api_key}

    def get_iata_code(self, city):
        """Returns IATA code for given city"""
        params = {
            "term": city,
            "locale": "en-US",
            "location_types": "airport",
            "limit": 1,
            "active_only": True,
        }
        response = requests.get(url=f"{self.endpoint}/locations/query", params=params, headers=self.header)
        response.raise_for_status()
        return response.json()["locations"][0]["id"]
