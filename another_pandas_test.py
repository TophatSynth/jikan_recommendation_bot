import json
import pandas as pd
import random as rd
import requests

data = [
    {
        "state": "Florida",
        "shortname": "FL",
        "info": {"governor": "Rick Scott"},
        "counties": [
            {"name": "Dade", "population": 12345},
            {"name": "Broward", "population": 40000},
            {"name": "Palm Beach", "population": 60000},
        ],
    },
    {
        "state": "Ohio",
        "shortname": "OH",
        "info": {"governor": "John Kasich"},
        "counties": [
            {"name": "Summit", "population": 1234},
            {"name": "Cuyahoga", "population": 1337},
        ],
    },
]


result = pd.json_normalize(
    data, "counties",["state", "shortname", ["info", "governor"]]
).to_string()
# print(result)

choice = rd.choice(data)
print(choice)


params = {"type":"tv", "filter":"bypopularity", "limit": 2}
response = requests.get(url="https://api.jikan.moe/v4/genres/anime", params=params)



with open("test.json", "rt") as file:
    data = json.load(file)

