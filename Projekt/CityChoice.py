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


def chosen_city(city):
    city = city.lower()
    url = "https://danepubliczne.imgw.pl/api/data/synop/station/" + city
    response = requests.get(url)
    info = json.loads(response.text)
    weather = Weather(info)

    return weather


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

    def __str__(self):
        show_all = vars(self)
        text = ""
        for key, value in show_all.items():
            part1 = f"{key} : {value}"
            text += f"{part1}  \n"

        return text
