import requests
import os
import datetime as dt


class FlightSearch:
    """Class responsible for talking with Flight Search API"""

    def __init__(self):
        self.endpoint = "https://api.tequila.kiwi.com"
        self.header = {"apikey": os.environ.get("TEQUILA_API_KEY")}

    def get_iata_code(self, city: str):
        """Returns IATA code for given city"""
        params = {
            "term": city,
            "locale": "en-US",
            "location_types": "city",
            "limit": 1,
            "active_only": True,
        }
        response = requests.get(url=f"{self.endpoint}/locations/query", params=params, headers=self.header)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def search_flight(self, fly_from: str, fly_to: str):
        tomorrow = dt.datetime.now() + dt.timedelta(days=1)
        in_six_months = dt.datetime.now() + dt.timedelta(days=180)
        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": in_six_months.strftime("%d/%m/%Y"),
            "flight_type": "round",
            "max_stopovers": 0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "adults": 1,
            "cur": "EUR",
            "limit": 1,
        }
        response = requests.get(url=f"{self.endpoint}/v2/search", params=params, headers=self.header)
        if response.status_code == 200:
            if len(response.json()["data"]) == 0:
                params["max_stopovers"] = 1
                response = requests.get(url=f"{self.endpoint}/v2/search", params=params, headers=self.header)
                if len(response.json()["data"]) == 0:
                    return None
            return response.json()
        return None
