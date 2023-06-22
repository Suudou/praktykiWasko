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
    for obj in data:
        city = obj.get('stacja')
        cities.append(city)
    return cities


def choosed_city(city):
    url = "https://danepubliczne.imgw.pl/api/data/synop/station/" + formatted_in
    response = requests.get(url)
    info = json.loads(response.text)
    print(info)
    return info


choice = input("wpisz nazwę miasta, bez polskich znaków \n")
formatted_in = choice.lower()
choosed_city(formatted_in)

