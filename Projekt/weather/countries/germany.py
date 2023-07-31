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
        return [station['name'] for station in self._get_all_cities()]
