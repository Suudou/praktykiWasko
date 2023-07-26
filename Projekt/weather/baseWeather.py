# klasa bazowa
import json
from abc import abstractmethod
from string import Template
import requests


class URLTemplate:
    def __init__(self, all_cities_url: str, specific_cities_url: str):
        self.ALL_CITIES_URL = Template(all_cities_url)
        self.SPECIFIC_CITIES_URL = Template(specific_cities_url)

    # metody protected
    def _get_all_cities(self, **kwargs) -> dict:
        # url = all_cities_url.substitute(**parameters)
        url = self.ALL_CITIES_URL.substitute(kwargs)
        response = requests.get(url)
        return json.loads(response.text)

    def _get_city_data(self, **kwargs) -> dict:
        # url = all_cities_url.substitute(**parameters)
        url = self.SPECIFIC_CITIES_URL.substitute(kwargs)
        response = requests.get(url)
        return json.loads(response.text)

    @abstractmethod
    def get_city_names(self) -> list:
        pass

    @abstractmethod
    def get_formatted_city_data(self, specific_city_name) -> dict:
        basic_weather_template = {
            'City': '',
            'Temperature': '',
            'Pressure': '',
            'Rainfall': '',
        }
        return basic_weather_template
