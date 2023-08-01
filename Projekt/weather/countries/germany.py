
from Projekt.weather.baseWeather import URLTemplate
import datetime
import requests

GERMAN_ALL_CITIES = "https://brightsky.dev/demo/cities.json"
GERMAN_SPECIFIC_CITY = "https://api.brightsky.dev/weather?lat=$lat&lon=$lon&date=$date&last_date=$last_date"


class GermanyWeather(URLTemplate):
    def __init__(self, all_cities_url: str, specific_cities_url: str):
        super().__init__(all_cities_url, specific_cities_url)

    def get_city_names(self) -> list:
        return [station['name'] for station in self._get_all_cities()]

    def __prepare_url_params(self, chosen_city):
        query_params = {}
    # Todo: write tests
        # Formatted date for url
        current_date = datetime.datetime.now()
        time_difference = datetime.timedelta(minutes=59, seconds=59, microseconds=999999)
        result_datetime = current_date - time_difference
        result_date = datetime.datetime.now().replace(minute=0, second=0, microsecond=0).isoformat()
        last_date = datetime.datetime.now()
        query_params["date"] = str(result_date)
        query_params["last_date"] = str(last_date)

        # matching query params for longitude and latitude
        for city in self._get_all_cities():
            if city["name"].lower() == chosen_city.lower():
                query_params["lat"] = city["lat"]
                query_params["lon"] = city["lon"]

        return query_params



