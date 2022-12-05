import os
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "KRK"

# Create data manager
data_manager = DataManager()
# Create flight searcher
flight_search = FlightSearch()
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
    flight_data = flight_search.search_flight(ORIGIN_CITY_IATA, row["iataCode"])
    if flight_data is not None:
        flight = FlightData(flight_data)
        print(flight.get_info_message())
        if flight.price < row["lowestPrice"]:
            notification_manager.send_message(flight.get_info_message())
