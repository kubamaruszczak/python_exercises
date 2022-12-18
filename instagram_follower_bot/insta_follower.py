import os
from selenium import webdriver

SIMILAR_ACCOUNT = "szymongodziek"
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self, username, password):
        pass

    def find_followers(self):
        return []

    def follow(self, to_follow):
        pass


follower_bot = InstaFollower()
follower_bot.login(USERNAME, PASSWORD)
followers = follower_bot.find_followers()
for follower in followers:
    follower_bot.follow(follower)
