import requests
import os

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": os.environ.get("PIXELA_TOKEN"),
    "username": "mariuszmtwc",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Set up a pixela account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
