import requests
import os
from bs4 import BeautifulSoup

URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37.657151767892316%2C%22north%22%3A37.893242656745365%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"


class PropertiesFinder:

    def __init__(self):
        # Get the website contents
        headers = {
            "User-Agent": os.environ.get("USER_AGENT"),
        }
        # Create a soup from the zillow contents
        response = requests.get(URL, headers=headers)
        zillow_contents = response.text
        self.soup = BeautifulSoup(zillow_contents, "html.parser")

    def get_links(self):
        links = []

        raw_links = self.soup.select(".property-card-data .property-card-link")
        for link in raw_links:
            link_text = link.get("href")
            if "zillow.com" not in link_text:
                links.append("https://www.zillow.com" + link_text)
            else:
                links.append(link_text)
        return links

    def get_prices(self):
        raw_prices = self.soup.select(".hRqIYX span")
        prices = [price.text.split("+")[0] for price in raw_prices]
        prices = [price.split("/")[0] for price in prices]
        return prices

    def get_addresses(self):
        raw_addresses = self.soup.select(".property-card-link address")
        addresses = [address.text for address in raw_addresses]
        return addresses

    def get_properties_data(self):
        addresses = self.get_addresses()
        prices = self.get_prices()
        links = self.get_links()

        # Create a properties info dict
        properties = {}
        for idx in range(len(links)):
            properties[idx] = {
                "address": addresses[idx],
                "price": prices[idx],
                "link": links[idx],
            }
        return properties
