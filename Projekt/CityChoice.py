import requests
import json

# 1 funkcja zwraca liste nazw miast
# 2 funkcja zwraca dane do miasta -> https://danepubliczne.imgw.pl/api/data/synop/station/jeleniagora ma zmieniać
# link dla odpowiedniego miasta
# drugi plik zrobić klase która ma pola i wartosci do pól, __str__


def cities_get():
    url = "https://danepubliczne.imgw.pl/api/data/synop"
    response = requests.get(url)
    data = json.loads(response.text)
    cities = []
    #choice = input("wpisz nazwę miasta\n")
    #formatted_in = choice.lower().capitalize()
    for obj in data:
        city = obj.get('stacja')
        cities.append(city)
    return cities
print(cities_get())

def choosed_city(choice):


