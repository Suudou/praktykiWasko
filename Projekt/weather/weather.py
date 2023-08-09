#from weather.countries.polish import PolishWeather
#import weather.countries.polish

from Projekt.weather.countries.polish import PolishWeather


# get_formatted_city_data wchodzi do weather, i zamieniam słownik w pola
# przypisać jednostki jako osobne pola

class Weather:
    def __init__(self, data: dict):
        self.data = {'city': data['City']}

        for key, value in data.items():
            if key != 'City':
                self.data[key] = {
                    'value': value,
                    'unit': self.get_unit(key)
                }

    def get_unit(self, key):
        units = {
            'Temperature': 'C',
            'Pressure': 'hPa',
            'Rainfall': 'mm',
            'Wind velocity': 'km/h',
            'Humidity': '%',
            'Date': 'CEST',
            'Hour': 'CEST'
        }
        return units.get(key, '')

    def __str__(self):
            return str(self.data)


polish_weather = PolishWeather()
temp = polish_weather.get_formatted_city_data('warszawa')
weather = Weather(temp)
print(weather)