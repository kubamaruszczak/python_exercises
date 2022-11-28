import requests
import smtplib
from time import sleep
from datetime import datetime

MY_LAT = 50.064651  # Your latitude
MY_LONG = 19.944981  # Your longitude

MY_MAIL = "your@email.com"
MY_PASSWORD = "app_password"


def is_iss_visible():
    """Returns Ture if your position is within +5 or -5 degrees of the ISS position and False otherwise"""
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        return True
    return False


def is_night():
    """Checks if there is currently dark and returns True or False appropriately"""
    # Get actual sunrise and sunset hours for my location
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # Extract current hours from received json
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 1
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 1

    current_hour = datetime.now().hour
    if current_hour <= sunrise or current_hour >= sunset:
        return True
    return False


def send_mail():
    """Sends mail that notifies that iss is visible on the sky"""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs=MY_MAIL,
                            msg="Subject:ISS Tracker\n\nLook up! ISS is visible on the sky!")


while True:
    # If the ISS is close to my current position and it is currently dark
    if is_iss_visible() and is_night():
        # Then send me an email to tell me to look up.
        send_mail()
    sleep(60)
