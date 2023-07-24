from string import Template
from fastapi import requests
import sys
from Projekt.weather import baseWeather

POLISH_ALL_CITIES = "https://danepubliczne.imgw.pl/api/data/synop"
POLISH_SPECIFIC_CITY = "https://danepubliczne.imgw.pl/api/data/synop/station/$cityname"
parameters = {}

all_polish_cities = baseWeather.URLTemplate.get_all_cities(Template(POLISH_ALL_CITIES), parameters)
# print([station.get('stacja') for station in all_polish_cities])


def city_names_list():
    city_names_list = []
    for station in all_polish_cities:
        city = station.get('stacja')
        city_names_list.append(city)
    return city_names_list


print(city_names_list())


"""#2 zmienne od templatów
# klasie potomnej
POLISH_ALL_CITIES = "https://danepubliczne.imgw.pl/api/data/synop"
POLISH_SPECIFIC_CITY = "https://danepubliczne.imgw.pl/api/data/synop/station/$cityname"

# To powinno być rozbite
# konstruktor klasy bazowej przyjmuje stringa
# konstruktor klasy potomnej zapewnia tego stringa
tmp = Template(POLISH_ALL_CITIES)
tmp2 = Template(POLISH_SPECIFIC_CITY)

print(get_all_cities(tmp, {}))
print(get_specific_cities(tmp2, cityname='hel'))


# klasa potomna - get_all_city_names
weather_data = get_all_cities(tmp, {}) # json ze wszystkim
print([station.get('stacja') for station in weather_data])
"""
