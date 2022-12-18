import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
        cookies_button = self.driver.find_element("class name", '_a9_1')
        cookies_button.click()
        sleep(2)
        username_input = self.driver.find_element("name", "username")
        username_input.send_keys(username)
        password_input = self.driver.find_element("name", "password")
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        sleep(5)

    def find_followers(self):
        side_bar_buttons = self.driver.find_elements("class name", "_aada")
        print(side_bar_buttons)
        for button in side_bar_buttons:
            print(button.text)
            if button.text == "Szukaj":
                button.click()
                break
        sleep(2)
        search_field = self.driver.find_element("class name", "_aauy")
        search_field.send_keys(SIMILAR_ACCOUNT)
        sleep(2)
        account = self.driver.find_element("class name", "_abm4")
        account.click()
        sleep(2)
        account_stats_bars = self.driver.find_elements("class name", "x1uw6ca5")
        account_stats_bars[1].click()
        sleep(2)
        all_followers = self.driver.find_elements("class name", "_aba8")
        return all_followers

    def follow(self, to_follow):
        pass


follower_bot = InstaFollower()
follower_bot.login(USERNAME, PASSWORD)
followers = follower_bot.find_followers()
print(len(followers))
for follower in followers:
    print(follower)
#     follower_bot.follow(follower)
