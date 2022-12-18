import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

SIMILAR_ACCOUNT = "szymongodziek"
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        self.driver.maximize_window()
        sleep(2)

    def login(self, username, password):
        # Agree with cookies
        cookies_button = self.driver.find_element("class name", '_a9_1')
        cookies_button.click()
        sleep(2)

        # Fill the username and password inputs
        username_input = self.driver.find_element("name", "username")
        username_input.send_keys(username)
        password_input = self.driver.find_element("name", "password")
        password_input.send_keys(password)
        sleep(2)

        # Log in into account
        password_input.send_keys(Keys.ENTER)
        sleep(5)

    def find_followers(self):
        # Navigate to desired account
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        sleep(2)

        # Click on followers bar to get a popup window
        account_stats_bars = self.driver.find_elements("class name", "x1uw6ca5")
        account_stats_bars[1].click()
        sleep(2)

        # Scroll down the window
        followers_popup = self.driver.find_element("class name", "_aano")
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
            sleep(2)

        all_followers = self.driver.find_elements("css selector", "._aba8 button")
        return all_followers

    def follow(self, follow_button):
        # Scroll element into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", follow_button)

        # Follow the person
        try:
            follow_button.click()
            sleep(1)
        except ElementClickInterceptedException:
            # If person was already followed - cancel unfollow action
            cancel_button = self.driver.find_element("class name", "_a9_1")
            cancel_button.click()
        sleep(1)


follower_bot = InstaFollower()
follower_bot.login(USERNAME, PASSWORD)
followers = follower_bot.find_followers()
print(len(followers))
for follower in followers:
    follower_bot.follow(follower)
