from properties_finder import PropertiesFinder

# Find properties info
properties = PropertiesFinder()
links = properties.get_links()
prices = properties.get_prices()
addresses = properties.get_addresses()

