
from weather.baseWeather import URLTemplate
import datetime
import requests

GERMAN_ALL_CITIES = "https://brightsky.dev/demo/cities.json"
GERMAN_SPECIFIC_CITY = "https://api.brightsky.dev/weather?lat=$lat&lon=$lon&date=$date&last_date=$last_date"


class GermanyWeather(URLTemplate):
    def __init__(self):

        super().__init__(GERMAN_ALL_CITIES, GERMAN_SPECIFIC_CITY)

    def get_city_names(self) -> list:
        return [station['name'] for station in self._get_all_cities()]

    def __prepare_url_params(self, chosen_city):
        query_params = {}
    # Todo: write tests, verify rounding errors
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

    def get_formatted_city_data(self, specific_city_name):
        basic_weather_template = super().get_formatted_city_data(specific_city_name)
        city_data = self._get_city_data(**self.__prepare_url_params(specific_city_name))
        german_weather_dict = basic_weather_template
        weather_data = city_data.get('weather', [])
        weather_info = weather_data[0]
        date_time_string = weather_info.get('timestamp')
        date = date_time_string[:10]
        time = date_time_string[11:19]
        german_weather_dict.update({
            'City': specific_city_name,
            'Temperature': {'value': weather_info.get('temperature'), 'unit': 'C'},
            'Pressure': {'value': weather_info.get('pressure_msl'), 'unit': 'hPa'},
            'Rainfall': {'value': weather_info.get('Precipitation'), 'unit': 'mm'},
            'Wind velocity': {'value': weather_info.get('wind_speed'), 'unit': 'kilometers_per_hour'},
            'Humidity': {'value': weather_info.get('relative_humidity'), 'unit': '%'},
            'Date': {'value': date, 'unit': 'CEST'},
            'Hour': {'value': time, 'unit': 'CEST'},
        })
        return german_weather_dict



