import os
from data_manager import DataManager
from flight_search import FlightSearch

sheet_endpoint = "https://api.sheety.co/a042454111d46a1f9daaa68e9f7ca593/flightDealsFinder/prices"
data_manager = DataManager(sheet_endpoint, os.environ.get("USERNAME"), os.environ.get("PASSWORD"))

flight_search = FlightSearch(os.environ.get("TEQUILA_API_KEY"))

sheet_data = data_manager.get_sheet()
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_iata_code(row["city"])
        data_manager.update_row(row)