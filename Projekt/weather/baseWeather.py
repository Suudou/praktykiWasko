# klasa bazowa
import json
from string import Template
import requests


class URLTemplate:
    def __init__(self, all_cities_url: str, specific_cities_url: str):
        self.ALL_CITIES_URL = Template(all_cities_url)
        self.SPECIFIC_CITIES_URL = Template(specific_cities_url)

    def get_all_cities(self, all_cities_url: Template, parameters: dict):
        # url = all_cities_url.substitute(**parameters)
        url = self.ALL_CITIES_URL.substitute(**parameters)
        response = requests.get(url)
        return json.loads(response.text)

    def get_specific_cities(self, specific_cities_url: Template, **kwargs) -> dict:
        # url = all_cities_url.substitute(**parameters)
        url = self.SPECIFIC_CITIES_URL.substitute(kwargs)
        response = requests.get(url)
        return json.loads(response.text)
