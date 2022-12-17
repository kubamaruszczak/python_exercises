from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import os

PROMISED_UP = 10
PROMISED_DOWN = 150
TWITTER_NAME = os.environ.get("TWITTER_NAME")
TWITTER_PASS = os.environ.get("TWITTER_PASS")


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        # Close the cookies window
        cookies_button = self.driver.find_element("xpath", '//*[@id="onetrust-accept-btn-handler"]')
        cookies_button.click()
        # Start internet test
        start_button = self.driver.find_element("xpath", '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_button.click()
        # Check when the test ends and update up and down speedss
        while True:
            try:
                result_data = self.driver.find_element("xpath", '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[1]/div/div/div[2]/div[2]/a')
            except NoSuchElementException:
                pass
            else:
                if len(result_data.text) > 0:
                    self.down = float(self.driver.find_element("class name", "download-speed").text)
                    self.up = float(self.driver.find_element("class name", "upload-speed").text)
                    break

        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        sleep(3)

        # Log in to Twitter
        username_input = self.driver.find_element("name", "text")
        username_input.send_keys(TWITTER_NAME)
        username_input.send_keys(Keys.ENTER)
        sleep(1)
        password_input = self.driver.find_element("name", "password")
        password_input.send_keys(TWITTER_PASS)
        password_input.send_keys(Keys.ENTER)

        # Fill a tweet text input
        sleep(2)
        tweet_input = self.driver.find_element("class name", 'public-DraftEditor-content')
        tweet_input.click()
        tweet_msg = f"Hey Internet Provider, why is my internet speed {self.down}down / {self.up}up?"
        tweet_input.send_keys(tweet_msg)

        # Post a tweet
        post_button = self.driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        post_button.click()

        self.driver.quit()
