import requests
import os
from twilio.rest import Client

TWILIO_NUM = "+123123123"
MY_NUM = "+321321321"


def will_rain_today() -> bool:
    """Returns True if it will rain in next 12 hours and False otherwise"""
    api_key = "your_api_key"
    owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
    weather_params = {
        "lat": 50.064651,
        "lon": 19.944981,
        "appid": os.environ.get("OWM_API_KEY"),
    }

    response = requests.get(url=owm_endpoint, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()
    today_weather = weather_data["list"][:5]  # weather for the next 12 hours
    for condition in today_weather:
        weather_code = int(condition["weather"][0]["id"])
        if weather_code < 600:
            return True
    return False


def send_sms():
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="It's going to rain today. Remember to bring an umbrella! ☔",
                                     from_=TWILIO_NUM,
                                     to=MY_NUM)
    print(message.status)


if will_rain_today():
    send_sms()
