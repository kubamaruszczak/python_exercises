import requests

MY_LAT = 50.064651
MY_LONG = 19.944981
API_KEY = "YOUR_API_KEY"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units": "metric",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
response.raise_for_status()
data = response.json()
print(data["list"][:8])  # one day weather with every 3 hour stamp
