from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

FORM_URL = "https://forms.gle/ps7qTw2132db9LET6"


class FormFiller:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def fill_form(self, answers):
        self.driver.get(FORM_URL)
        sleep(2)
        # Find inputs from the form
        inputs = self.driver.find_elements("css selector", ".Xb9hP input")
        address_input = inputs[0]
        price_input = inputs[1]
        link_input = inputs[2]

        # Fill out the form
        address_input.send_keys(answers["address"])
        price_input.send_keys(answers["price"])
        link_input.send_keys(answers["link"])

        # Submit the form
        submit_button = self.driver.find_element("xpath",
                                                 '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit_button.click()
        sleep(1)
