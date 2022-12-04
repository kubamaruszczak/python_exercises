import os
from twilio.rest import Client


class NotificationManager:
    """Class responsible for sending sms notification"""

    def __init__(self, to_num):
        self.from_num = "+19497870937"
        self.to_num = to_num
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, text):
        message = self.client.messages.create(body=text,
                                              from_=self.from_num,
                                              to=self.to_num)
        print(message.status)
