import requests
import datetime as dt
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_date():
    user_input = input("Which year od you want to travel to? Type the date in this format YYYY-MM-DD: ")
    try:
        dt.datetime.strptime(user_input, "%Y-%m-%d")
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD. Try again.")
        return get_date()
    else:
        return user_input


# Get user input with the date
date = get_date()

# Get billboard hot 100 website contents
billboard_url = "https://www.billboard.com/charts/hot-100"
response = requests.get(url=f"{billboard_url}/{date}")
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

# Get top 100 songs titles and artists
li_tags = soup.find_all(name="li", class_="o-chart-results-list__item")
songs = []
for tag in li_tags:
    if tag.find(name="h3", class_="c-title") is not None:
        title = tag.find(name="h3", class_="c-title").getText().strip()
        artist = tag.find(name="span", class_="c-label").getText().strip()
        songs.append(f"{artist} {title}")

# Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private"))
# Creating private playlist with entered date
user_id = sp.me()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"Top 100 Songs of {date}", public=False)
playlist_id = playlist["id"]

# Searching for the songs URIs
songs_uris = []
for song in songs:
    result = sp.search(song, type="track", limit=1)
    try:
        songs_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        continue
    except KeyError:
        continue

# Add songs to playlist
sp.playlist_add_items(playlist_id=playlist_id, items=songs_uris)
