import datetime
from weather.baseWeather import URLTemplate

AMERICAN_ALL_CITIES = "http://127.0.0.1:8000/us/$year/$month/$day?hour=$hour"
AMERICAN_SPECIFIC_CITY = "http://127.0.0.1:8000/us/$year/$month/$day?hour=$hour"
class AmericanWeather(URLTemplate):
    def __init__(self):
        super().__init__(AMERICAN_ALL_CITIES, AMERICAN_SPECIFIC_CITY)

    def __get_formatted_datetime(self):
        query_params = {}
        current_date = datetime.datetime.now()
        query_params["year"] = current_date.year
        query_params["month"] = current_date.month
        query_params["day"] = current_date.day
        query_params["hour"] = current_date.strftime("%I%p")
        return query_params

    def get_city_names(self) -> list:
        return [station['location']['city'] for station in self._get_all_cities(**self.__get_formatted_datetime())]

    def get_formatted_city_data(self, specific_city_name):
        basic_weather_template = super().get_formatted_city_data(specific_city_name)
        city_data = self._get_city_data(**self.__get_formatted_datetime())

        american_weather_dict = basic_weather_template

        def find_station():
            for station in city_data:
                if station['location']['city'].lower().replace(" ", "_") == specific_city_name.lower():
                    return station
            return None

        station_data = find_station()
        weather_data = station_data.get('weather')

        def split_unit_and_value(key: str, offset: int):
            return {'value': weather_data.get(key)[:-offset], 'unit':  weather_data.get(key)[-offset:]}

        american_weather_dict.update({
            'City': specific_city_name,
            'Temperature': split_unit_and_value('temperature', 1),
            'Pressure': split_unit_and_value('pressure', 2),
            'Rainfall': split_unit_and_value('rainfall', 2),
            'Wind velocity': split_unit_and_value('wind_speed', 3),
            'Humidity': split_unit_and_value('humidity', 1),
            'Date': {'value': station_data['time']['date'], 'unit': 'CEST'},
            'Hour': {'value': station_data['time']['time'], 'unit': 'CEST'}
        })
        return american_weather_dict

