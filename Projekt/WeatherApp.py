import json
import requests
import tkinter
url = "https://danepubliczne.imgw.pl/api/data/synop"
response = requests.get(url)
data = json.loads(response.text)
miasto = input("wpisz nazwę miasta\n")
formatted_in = miasto.lower().capitalize()

for city in data:
    if city['stacja'] == formatted_in:
        for key, value in city.items():
            print(key, ":", value)


