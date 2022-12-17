from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

PROMISED_UP = 10
PROMISED_DOWN = 150


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
        self.driver.get("https://twitter.com/")

        sleep(600)  # debug

