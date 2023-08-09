from string import Template
from fastapi import requests
import json

from Projekt.weather.baseWeather import URLTemplate

POLISH_ALL_CITIES = "https://danepubliczne.imgw.pl/api/data/synop"
POLISH_SPECIFIC_CITY = "https://danepubliczne.imgw.pl/api/data/synop/station/$cityname"


class PolishWeather(URLTemplate):
    def __init__(self):
        all_cities_url = "https://danepubliczne.imgw.pl/api/data/synop"
        specific_cities_url = "https://danepubliczne.imgw.pl/api/data/synop/station/$cityname"

        super().__init__(all_cities_url, specific_cities_url)

    def get_city_names(self, ) -> list:
        city_names_list = []
        all_cities = self._get_all_cities()
        for station in all_cities:
            city = station.get('stacja')
            city_names_list.append(city)
        return city_names_list

    def get_formatted_city_data(self, specific_city_name) -> dict:
        basic_weather_template = super().get_formatted_city_data(specific_city_name)
        city_data = self._get_city_data(cityname=specific_city_name)
        polish_weather_dict = basic_weather_template
        polish_weather_dict.update({
            'City': city_data.get('stacja'),
            'Temperature': {'value': city_data.get('temperatura'), 'unit': 'C'},
            'Pressure': {'value': city_data.get('cisnienie'), 'unit': 'hPa'},
            'Rainfall': {'value': city_data.get('suma_opadu'), 'unit': 'mm'},
            'Wind velocity': {'value': city_data.get('predkosc_wiatru'), 'unit': 'kilometers_per_hour'},
            'Humidity': {'value': city_data.get('wilgotnosc_wzgledna'), 'unit': '%'},
            'Date': {'value': city_data.get('data_pomiaru'), 'unit': 'CEST'},
            'Hour': {'value': city_data.get('godzina_pomiaru'), 'unit': 'CEST'},
                })
        return polish_weather_dict



#Przykładowe wywołanie

#polish_weather = PolishWeather(POLISH_ALL_CITIES, POLISH_SPECIFIC_CITY)
#temp = polish_weather.get_formatted_city_data('warszawa')
#print(temp)

