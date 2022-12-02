import requests
import os

USERNAME = "mariuszmtwc"
TOKEN = os.environ.get("PIXELA_TOKEN")

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
    "id": "graph1",
    "name": "Python Learning",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu",  # green
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_endpoint = f"/v1/users/{USERNAME}/graphs"
response = requests.post(url=f"{pixela_url}{graph_endpoint}", json=graph_config, headers=headers)
print(response.text)
