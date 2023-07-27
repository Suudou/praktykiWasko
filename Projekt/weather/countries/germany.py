import os
import pandas as pd
from Projekt.weather.baseWeather import URLTemplate


class GermanyWeather(URLTemplate):

    def get_city_names(self, ) -> list:
        file_path = 'C:\\Users\\l.sudol\\PycharmProjects\\lsudol\\Projekt\\weather\\countries\\german_data.xls'
        print("git") if os.path.exists(file_path) else print("źle")
        german_data = pd.read_excel(file_path)
        # Wyciągnięcie jednej kolumny (np. kolumna z nazwami stacji)
        station_names = german_data['Stations-Name']
        german_cities_list = station_names.tolist()
        return german_cities_list




