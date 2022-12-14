from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element("id", "cookie")

while True:
    cookie.click()
