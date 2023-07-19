# klasa bazowa
import json
from string import Template

from fastapi import requests


def get_all_cities(ALL_CITIES_URL:Template, parameters: dict):
    # url = ALL_CITIES_URL.substitute(**parameters)
    url = ALL_CITIES_URL.substitute(**parameters)
    response = requests.get(url)
    return json.loads(response.text)

def get_specific_cities(SPECIFIC_CITIES_URL:Template, **kwargs)->dict:
    # url = ALL_CITIES_URL.substitute(**parameters)
    url = SPECIFIC_CITIES_URL.substitute(kwargs)
    response = requests.get(url)
    return json.loads(response.text)

#kontruktor przyjmuje 2 stringi, "url"e ALL_CITIES_URL:Template(url)