import pandas as pd
import requests
import json
import random

class Search():
    def __init__(self) -> None:
        pass

    def get_category(self) -> str:
        return input("Which category would you like to search in?: \n- ")

    def check_category_valid(self, category: str) -> bool:
        categories = {"t":"top", "g":"genre", "s":"season"}
        try:
            return categories[category]
        except KeyError:
            print("Not one of the available options. Try again! ")
            return False

    def get_filter(self) -> str:
        return input("Input filter: \n-")

    def search_by_top(self) -> pd.DataFrame:
        params = {"filter":"bypopularity", "page":"1"}
        response = requests.get("https://api.jikan.moe/v4/top/anime", params=params)
        response.raise_for_status()
        return response.json()

    def search_by_genre(self, filter: str) -> pd.DataFrame:
        genre_id = 0

        genre_list_params = {"filter":"genres"}
        genre_list_response = requests.get("https://api.jikan.moe/v4/genres/anime", params=genre_list_params)
        genre_list_response.raise_for_status()
        genre_list = genre_list_response.json()


        for data in genre_list["data"]:
            if filter.lower() == data.get("name").lower():
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


    def search_by_producer(self, filter: str) -> pd.DataFrame:
        pass
    def search_by_season(self, filter: str) -> pd.DataFrame:
        pass
    
    def choose_random_anime(self, data: pd.DataFrame) -> pd.DataFrame:
        random.choice(data)

    def print_anime(self, data: pd.DataFrame) -> None:
        print(f"""
            Title: {data['data'][0]['title_english']}
            URL: {data['data'][0]['url']}
            Rating: {data['data'][0]['rating']}

            Synopsis: 
            {data['data'][0]['synopsis']}
            """)

    def check_repeat_search(self) -> bool:
        while True:
            ans = input("Would you like to run another search? (y/n)")
            if ans == "y":
                return True
            elif ans == "n":
                return False
            else:
                continue

    def start_search(self) -> None:
        while True:
            category = self.get_category()

            if self.check_category_valid(category) == False:
                continue
            else:
                pass

            filter = self.get_filter()

            try:
                if category == "top":
                    results = self.search_by_top()
                elif category == "genre":
                    results = self.search_by_genre(filter)
                elif category == "season":
                    results = self.search_by_season(filter)
                elif category == "producer":
                    results = self.search_by_producer(filter)
            except requests.HTTPError as err:
                print(err)
                continue
            else:
                pass

            chosen_anime = self.choose_random_anime(results)

            self.print_anime(chosen_anime)

            if self.check_repeat_search():
                continue
            else:
                print("Have fun watching! :D")
                break

if __name__ == "__main__":
    search = Search()
    search.start_search()