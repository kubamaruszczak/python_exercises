import selenium.webdriver.chromium.webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3279714761&f_AL=true&f_I=4%2C6&f_JT=F%2CC&f_WT=2&geoId=105072130&keywords=Programista%20Python&location=Polska&refresh=true&sortBy=R")
sleep(2)

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
sleep(20)  # wait for the page to properly load up and manually pass the security check

# Scroll jobs list all the way down to load all offers
jobs = driver.find_elements("css selector", ".scaffold-layout__list-container .job-card-container--clickable")
driver.execute_script("arguments[0].scrollIntoView(true);", jobs[0])
prev_len = 0
while True:
    jobs = driver.find_elements("css selector", ".scaffold-layout__list-container .jobs-search-results__list-item")
    if len(jobs) != prev_len:
        driver.execute_script("arguments[0].scrollIntoView(true);", jobs[-1])
        prev_len = len(jobs)
    else:
        print(f"Done scrolling. Offers on this page: {len(jobs)}")
        break

# Apply for all jobs
for job in jobs:
    job.click()
    driver.execute_script("arguments[0].scrollIntoView(true);", job)
    sleep(3)
    save_button = driver.find_element("class name", "jobs-save-button")
    try:
        save_button.click()
    except NoSuchElementException:
        continue
    except ElementClickInterceptedException:
        continue
    else:
        sleep(2)

driver.quit()
