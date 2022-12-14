from selenium import webdriver
import datetime as dt

END_GAME_AFTER = 600
BUY_UPGRADE_AFTER = 6

driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element("id", "cookie")

game_start = dt.datetime.now()
prev_time = game_start
while True:
    cookie.click()
    now = dt.datetime.now()

    if (now - game_start).total_seconds() > END_GAME_AFTER:
        cookie_per_second = driver.find_element("id", "cps")
        print(cookie_per_second.text)
        break

    if (now - prev_time).total_seconds() > BUY_UPGRADE_AFTER:
        prev_time = now

        # Buy available upgrade
        upgrades = driver.find_elements("css selector", "#store div b")
        my_money = int(driver.find_element("id", "money").text.replace(",", ""))
        for upgrade in upgrades[::-1]:
            if len(upgrade.text) > 0:
                price = int(upgrade.text.split(" - ")[1].replace(",", ""))
                if my_money >= price:
                    upgrade.click()
                    break

