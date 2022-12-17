from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import os

driver = webdriver.Chrome()
driver.get("https://tinder.com/")

sleep(1)
agree_cookies = driver.find_element("xpath", "//*[@id='q888578821']/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]")
agree_cookies.click()

sleep(1)
log_in = driver.find_element("xpath", "//*[@id='q888578821']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")
log_in.click()

sleep(1)
via_fb = driver.find_element("xpath", "//*[@id='q-839802255']/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]")
via_fb.click()

sleep(1)
windows = driver.window_handles
fb_window = windows[1]
driver.switch_to.window(fb_window)
sleep(1)
fb_cookies = driver.find_element("css selector", "._9xo5 button")
fb_cookies.click()
email_input = driver.find_element("name", "email")
email_input.send_keys(os.environ.get("EMAIL"))
password_input = driver.find_element("name", "pass")
password_input.send_keys(os.environ.get("PASSWORD"))
password_input.send_keys(Keys.ENTER)

sleep(600)
driver.close()
