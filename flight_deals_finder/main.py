import os
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# Create data manager
sheet_endpoint = "https://api.sheety.co/a042454111d46a1f9daaa68e9f7ca593/flightDealsFinder/prices"
data_manager = DataManager(sheet_endpoint, os.environ.get("USERNAME"), os.environ.get("PASSWORD"))

# Create flight searcher
flight_search = FlightSearch("London")

# Create notification manager
notification_manager = NotificationManager(os.environ.get("MY_NUM"))

# Get data from the sheet
sheet_data = data_manager.get_sheet()
for row in sheet_data:
    # Fill IATA codes if needed
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_iata_code(row["city"])
        data_manager.update_row(row)
    # Check for flights
    flight_data = flight_search.search_flight(row["iataCode"])
    if flight_data is not None:
        flight = FlightData(flight_data)
        print(flight.get_info_message())
        if flight.price < row["lowestPrice"]:
            notification_manager.send_message(flight.get_info_message())
