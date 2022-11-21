import requests

url = "https://www.kinopoisk.ru/lists/movies/top250/"
r = requests.get(url)
r.text
