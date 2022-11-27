import smtplib
import pandas
import datetime as dt
from random import randint

# email data
MY_EMAIL = "youremail@mail.com"
PASSWORD = "app_password"

# Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
data = pandas.read_csv("birthdays.csv", index_col=0)

# Find all persons who have birthday today
birthday_people = data[data.month == today.month]  # Check for the month
birthday_people = birthday_people[birthday_people.day == today.day]  # Check for the day

if len(birthday_people) > 0:
    for (_, person) in birthday_people.iterrows():
        # Choose random letter and replace name placeholder with person name
        letter_num = randint(1, 3)
        with open(f"letter_templates/letter_{letter_num}.txt") as letter_file:
            letter_template = letter_file.read()
            letter = letter_template.replace("[NAME]", person.name)

        # Send the letter to the person
        with smtplib.SMTP("your.smtp.addr") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person.email,
                msg=f"Subject:Happy Birthday!\n\n{letter}"
            )
