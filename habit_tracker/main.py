import requests
import os
from datetime import datetime

USERNAME = "mariuszmtwc"
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"

pixela_url = "https://pixe.la"


def create_account(username: str, token: str):
    """Create pixela account for given username and token"""
    user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    create_user_endpoint = "/v1/users"
    response = requests.post(url=f"{pixela_url}{create_user_endpoint}", json=user_params)
    print(response.text)


def create_graph(username: str, graph_id: str, name: str, unit: str, value_type: str, color: str):
    """Creates piexla graph with given parameters"""
    graph_config = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": value_type,
        "color": color,  # green
    }
    headers = {
        "X-USER-TOKEN": TOKEN,
    }
    graph_endpoint = f"/v1/users/{username}/graphs"
    response = requests.post(url=f"{pixela_url}{graph_endpoint}", json=graph_config, headers=headers)
    print(response.text)


def post_pixel(username: str, graph_id: str, date: str, quantity: str):
    """Posts a pixel for a given date and quantity"""
    pixel_params = {
        "date": date,
        "quantity": quantity,
    }
    headers = {
        "X-USER-TOKEN": TOKEN,
    }
    post_pixel_endpoint = f"/v1/users/{username}/graphs/{graph_id}"
    response = requests.post(url=f"{pixela_url}{post_pixel_endpoint}", json=pixel_params, headers=headers)
    print(response.text)


def update_pixel(username: str, graph_id: str, date: str, new_quantity: str):
    new_pixel_params = {
        "quantity": new_quantity
    }
    headers = {
        "X-USER-TOKEN": TOKEN,
    }
    update_pixel_endpoint = f"/v1/users/{username}/graphs/{graph_id}/{date}"
    print(update_pixel_endpoint)
    response = requests.put(url=f"{pixela_url}{update_pixel_endpoint}", json=new_pixel_params, headers=headers)
    print(response.text)


# create_account(USERNAME, TOKEN)
# create_graph(USERNAME, GRAPH_ID, "Python Learning", "minutes", "int", "shibafu")
today = datetime.now().strftime("%Y%m%d")
# post_pixel(USERNAME, GRAPH_ID, today, "90")
update_pixel(USERNAME, GRAPH_ID, today, "120")
