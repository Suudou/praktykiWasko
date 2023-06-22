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

    return info


class Weather:
    def __init__(self, city_info):
        self.city = city_info.get('stacja')
        self.date = city_info.get('data_pomiaru')
        self.time = city_info.get('godzina_pomiaru')
        self.temp = city_info.get('temperatura')
        self.wind = city_info.get('predkosc_wiatru')
        self.humidity = city_info.get('wilgotnosc_wzgledna')
        self.rain = city_info.get('suma_opadu')
        self.pressure = city_info.get('cisnienie')


choice = input("wpisz nazwę miasta, bez polskich znaków \n")
formatted_in = choice.lower()
city_info = choosed_city(formatted_in)
weather = Weather(choosed_city(formatted_in))
print(weather)