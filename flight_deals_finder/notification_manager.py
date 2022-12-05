import os
from twilio.rest import Client
from smtplib import SMTP


class NotificationManager:
    """Class responsible for sending sms notification"""

    def __init__(self, to_num):
        # SMS
        self.from_num = "+19497870937"
        self.to_num = to_num
        self.client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
        # EMAIL
        self.from_email = os.environ.get("MY_EMAIL")
        self.email_password = os.environ.get("EMAIL_PASSWORD")

    def send_message(self, text):
        message = self.client.messages.create(body=text,
                                              from_=self.from_num,
                                              to=self.to_num)
        print(message.status)

    def send_emails(self, emails: list, text: str):
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.from_email, password=self.email_password)
            for email in emails:
                connection.sendmail(from_addr=self.from_email,
                                    to_addrs=email,
                                    msg=f"Subject:New Low Price Flight!\n\n{text}")
