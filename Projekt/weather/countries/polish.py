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

