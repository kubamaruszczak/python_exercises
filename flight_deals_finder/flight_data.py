class FlightData:
    """Class responsible for structuring the flight data"""

    def __init__(self, flight_data):
        # Cities info
        self.fly_from_code = flight_data["data"][0]["flyFrom"]
        self.fly_from_city = flight_data["data"][0]["cityFrom"]
        self.fly_to_code = flight_data["data"][0]["flyTo"]
        self.fly_to_city = flight_data["data"][0]["cityTo"]
        # Price info
        self.price = flight_data["data"][0]["price"]
        self.currency = flight_data["currency"]
        # Dates info
        self.departure_date = flight_data["data"][0]["route"][0]["local_departure"].split("T")[0]
        self.return_date = flight_data["data"][0]["route"][-1]["local_departure"].split("T")[0]
        # Optional stopovers info
        self.stopovers = 0
        self.via_city = ""
        self.via_city_code = ""
        if len(flight_data["data"][0]["route"]) > 2:
            self.stopovers = 1
            self.via_city = flight_data["data"][0]["route"][1]["cityFrom"]
            self.via_city_code = flight_data["data"][0]["route"][1]["flyFrom"]

    def get_info_message(self):
        """Returns message that consists essential flight data"""
        message = f"Only {self.price} {self.currency} to fly " \
                  f"from {self.fly_from_city}-{self.fly_from_code} to {self.fly_to_city}-{self.fly_to_code}, " \
                  f"from {self.departure_date} to {self.return_date}"
        if self.stopovers > 0:
            message += f"\nFlight has {self.stopovers} stopover, via {self.via_city}-{self.via_city_code}"
        return message
