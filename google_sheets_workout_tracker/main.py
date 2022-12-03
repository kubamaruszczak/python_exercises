import os
import requests
import datetime as dt


def get_exercise_data(exercises: str):
    nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    auth = {
        "x-app-id": os.environ.get("APP_ID"),
        "x-app-key": os.environ.get("API_KEY")
    }
    body = {
        "query": f"{exercises}"
    }
    response = requests.post(url=nutritionix_endpoint, json=body, headers=auth)
    response.raise_for_status()
    return response.json()["exercises"]


def post_exercise_to_sheets(exercise_name: str, duration: str, calories: str):
    auth = {
        "Authorization": f"Bearer {os.environ.get('TOKEN')}",
    }
    body = {
        "workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise_name.title(),
            "duration": duration,
            "calories": calories,
        }
    }
    response = requests.post(url=os.environ.get("SHEET_ENDPOINT"), json=body, headers=auth)
    print(response.text)


user_input = input("Tell which exercises you did: ")
exercises = get_exercise_data(user_input)

for exercise in exercises:
    post_exercise_to_sheets(exercise["name"], exercise["duration_min"], exercise["nf_calories"])
