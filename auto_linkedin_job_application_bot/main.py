from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3386933222&f_AL=true&f_WT=2&geoId=105072130&keywords=Programista%20Python&location=Polska&refresh=true&sortBy=R")

# Sing in to LinkedIn
sing_in_link = driver.find_element("link text", "Sign in")
sing_in_link.click()
# Fill up the email field
email_input = driver.find_element("name", "session_key")
email_input.send_keys(os.environ.get("EMAIL"))
# Fill up the password and log in
password_input = driver.find_element("name", "session_password")
password_input.send_keys(os.environ.get("PASSWORD"))
password_input.send_keys(Keys.ENTER)

sleep(10)
driver.quit()