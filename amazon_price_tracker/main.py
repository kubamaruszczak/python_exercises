import os
from requests import get
from bs4 import BeautifulSoup
from smtplib import SMTP

price_threshold = 120  # $
product_name = "White FOX MTB Helmet"

# Get product data from Amazon
product_url = "https://www.amazon.com/RACING-Youth-Rampage-Mountain-Helmet/dp/B08SG9HQXN/ref=cs_sr_dp?crid=3E3FS83PZQBHD&keywords=fox%2Bhelmet%2Bwhite&qid=1670917617&sprefix=fox%2Bhelmet%2Bwhi%2Caps%2C165&sr=8-2&th=1&psc=1"
headers = {
    "User-Agent": os.environ.get("USER_AGENT"),
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
}
response = get(url=product_url, headers=headers)
response.raise_for_status()
amazon_contents = response.text

# Get the price product using bs4
soup = BeautifulSoup(amazon_contents, "html.parser")
price_decimal = soup.find(name="span", class_="a-price-whole").getText()
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()
price = float(price_decimal + price_fraction)

# Send me an email when the product price is below defined threshold
if price < price_threshold:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        my_email = os.environ.get("EMAIL")
        connection.login(user=my_email,
                         password=os.environ.get("PASSWORD"))
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:{product_name} price alert!\n\n"
                                f"{product_name} price is now lower than {price_threshold} $\n"
                                f"{product_url}")


