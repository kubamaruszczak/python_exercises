import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

billboard_url = "https://www.billboard.com/charts/hot-100"

# Get user input with the date
# date = input("Which year od you want to travel to? Type the date in this format YYYY-MM-DD: ")
date = "2022-12-10"  # debug

# Get billboard hot 100 website contents
response = requests.get(url=f"{billboard_url}/{date}")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
li_tags = soup.find_all(name="li", class_="o-chart-results-list__item")
titles = [tag.find(name="h3", class_="c-title").getText().strip() for tag in li_tags
          if tag.find(name="h3", class_="c-title") is not None]

# Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])