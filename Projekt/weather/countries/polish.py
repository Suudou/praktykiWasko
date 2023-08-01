from string import Template
from fastapi import requests
import json

from Projekt.weather.baseWeather import URLTemplate

POLISH_ALL_CITIES = "https://danepubliczne.imgw.pl/api/data/synop"
POLISH_SPECIFIC_CITY = "https://danepubliczne.imgw.pl/api/data/synop/station/$cityname"


class PolishWeather(URLTemplate):
    def __init__(self, all_cities_url: str, specific_cities_url: str):
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
            'Temperature': city_data.get('temperatura'),
            'Pressure': city_data.get('cisnienie'),
            'Rainfall': city_data.get('suma_opadu'),
            'Wind velocity': city_data.get('predkosc_wiatru'),
            'Humidity': city_data.get('wilgotnosc_wzgledna'),
            'Date': city_data.get('data_pomiaru'),
            'Hour': city_data.get('godzina_pomiaru'),
                })
        return polish_weather_dict


#Przykładowe wywołanie

polish_weather = PolishWeather(POLISH_ALL_CITIES, POLISH_SPECIFIC_CITY)
#temp = polish_weather.get_formatted_city_data('warszawa')
#print(temp)

