import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
empire_webpage = response.text
soup = BeautifulSoup(empire_webpage, "html.parser")
movies = [tag.getText() for tag in soup.find_all(name="h3", class_="title")]

with open("movies.txt", mode="w") as file:
    for movie in movies[::-1]:
        file.write(f"{movie}\n")
