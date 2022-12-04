import os
from data_manager import DataManager

sheet_endpoint = "https://api.sheety.co/a042454111d46a1f9daaa68e9f7ca593/flightDealsFinder/prices"
data_manager = DataManager(sheet_endpoint, os.environ.get("USERNAME"), os.environ.get("PASSWORD"))
data_manager.get_sheet()
data_manager.update_sheet()
