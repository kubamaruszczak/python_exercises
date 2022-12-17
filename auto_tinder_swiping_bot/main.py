from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep
import os

driver = webdriver.Chrome()
driver.get("https://tinder.com/")

# Agree to cookies
sleep(1)
agree_cookies = driver.find_element("xpath", "//*[@id='q888578821']/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]")
agree_cookies.click()

# Log in via facebook
sleep(1)
log_in = driver.find_element("xpath", "//*[@id='q888578821']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")
log_in.click()

sleep(1)
via_fb = driver.find_element("xpath", "//*[@id='q-839802255']/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]")
via_fb.click()

sleep(1)
windows = driver.window_handles
tinder_window = windows[0]
fb_window = windows[1]
driver.switch_to.window(fb_window)
sleep(1)
fb_cookies = driver.find_element("css selector", "._9xo5 button")
fb_cookies.click()
email_input = driver.find_element("name", "email")
email_input.send_keys(os.environ.get("EMAIL"))
password_input = driver.find_element("name", "pass")
password_input.send_keys(os.environ.get("PASSWORD"))
sleep(2)
password_input.send_keys(Keys.ENTER)

# Agree to location pop up
driver.switch_to.window(windows[0])
sleep(5)
location_button = driver.find_element("xpath", '//*[@id="q-839802255"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
location_button.click()

# Disagree to notification pop up
sleep(5)
notifications_button = driver.find_element("xpath", '//*[@id="q-839802255"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
notifications_button.click()

# Close pop up with dark mode
sleep(2)
dark_mode_close = driver.find_element("xpath", '//*[@id="q-839802255"]/main/div/div[2]/button/svg/path')
dark_mode_close.click()

for n in range(100):
    sleep(1.5)

    try:
        like_button = driver.find_element("xpath", '//*[@id="q888578821"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span/span/svg/path')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element("css selector" ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.close()
