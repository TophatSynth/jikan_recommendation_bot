import requests 
import pandas as pd

example_genre = "Action"
genre_id = 0

genre_list_params = {"filter":"genres"}
genre_list_response = requests.get("https://api.jikan.moe/v4/genres/anime", params=genre_list_params)
genre_list_response.raise_for_status()
genre_list = genre_list_response.json()


for data in genre_list["data"]:
    if example_genre.lower() == data.get("name").lower():
        genre_id = data["mal_id"]
        break
    else:
        pass

if genre_id == 0:
    raise requests.HTTPError

anime_search_params = {"page": 1, "genres":f"{genre_id}"}
anime_search_response = requests.get("https://api.jikan.moe/v4/anime", params=anime_search_params)
anime_search_response.raise_for_status()
return anime_search_response.json()

