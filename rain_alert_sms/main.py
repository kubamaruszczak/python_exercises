import requests


def will_rain_today():
    """Returns True if it will rain in next 12 hours and False otherwise"""
    api_key = "YOUR_API_KEY"
    opw_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
    weather_params = {
        "lat": 50.064651,
        "lon": 19.944981,
        "appid": api_key,
    }

    response = requests.get(url=opw_endpoint, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()
    today_weather = weather_data["list"][:5]  # weather for the next 12 hours
    for condition in today_weather:
        weather_code = condition["weather"][0]["id"]
        if weather_code < 600:
            return True
    return False


if will_rain_today():
    print("You will need an umbrella.")
else:
    print("You are fine.")
