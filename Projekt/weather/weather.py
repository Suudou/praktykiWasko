from Projekt.weather.countries.polish import PolishWeather
import Projekt.weather.countries.polish

# get_formatted_city_data wchodzi do weather, i zamieniam słownik w pola


class Weather:
    def __init__(self, **kwargs):
        self.data = {}
        for key, value in kwargs.items():
            self.data[key] = value

