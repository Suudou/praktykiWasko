import os
import pandas as pd
from Projekt.weather.baseWeather import URLTemplate
import datetime
import requests


GERMAN_SPECIFIC_CITY = "https://api.brightsky.dev/weather?$cityname"
GERMAN_ALL_CITIES = "https://brightsky.dev/demo/cities.json"


class GermanyWeather(URLTemplate):
    def __init__(self, all_cities_url: str, specific_cities_url: str):
        super().__init__(all_cities_url, specific_cities_url)

    def get_city_names(self) -> list:
        # city_names_list = []
        all_cities = self._get_all_cities()
        city_names_list = [station['name'] for station in all_cities]
        return city_names_list
