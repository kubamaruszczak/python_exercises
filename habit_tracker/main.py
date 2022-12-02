import requests
import os
from datetime import datetime

USERNAME = "mariuszmtwc"
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"

pixela_url = "https://pixe.la"

# Create a pixela account
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# create_user_endpoint = "/v1/users"
# response = requests.post(url=f"{pixela_url}{create_user_endpoint}", json=user_params)
# print(response.text)

# Set up a graph
graph_config = {
    "id": GRAPH_ID,
    "name": "Python Learning",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu",  # green
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# graph_endpoint = f"/v1/users/{USERNAME}/graphs"
# response = requests.post(url=f"{pixela_url}{graph_endpoint}", json=graph_config, headers=headers)
# print(response.text)

# Post a pixel
pixel_params = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "120",
}

post_pixel_endpoint = f"/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=f"{pixela_url}{post_pixel_endpoint}", json=pixel_params, headers=headers)
print(response.text)
