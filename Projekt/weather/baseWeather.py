# klasa bazowa
import json
from string import Template
import requests


class URLTemplate:
    def __init__(self, all_cities_url: Template, specific_cities_url: Template):
        self.ALL_CITIES_URL = all_cities_url
        self.SPECIFIC_CITIES_URL = specific_cities_url

        def get_all_cities(all_cities_url: Template, parameters: dict):
            # url = all_cities_url.substitute(**parameters)
            url = all_cities_url.substitute(**parameters)
            response = requests.get(url)
            return json.loads(response.text)

        def get_specific_cities(specific_cities_url: Template, **kwargs) -> dict:
            # url = all_cities_url.substitute(**parameters)
            url = specific_cities_url.substitute(kwargs)
            response = requests.get(url)
            return json.loads(response.text)


#kontruktor przyjmuje 2 stringi, "url"e all_cities_url:Template