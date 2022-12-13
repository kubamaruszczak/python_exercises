import os
from requests import get
from bs4 import BeautifulSoup

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

