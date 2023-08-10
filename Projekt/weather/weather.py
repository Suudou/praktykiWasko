#from weather.countries.polish import PolishWeather
#import weather.countries.polish

from weather.countries.polish import PolishWeather


# get_formatted_city_data wchodzi do weather, i zamieniam słownik w pola
# przypisać jednostki jako osobne pola

class Weather:
    def __init__(self, data: dict):
        self.City = data.get('City')
        self.Temperature_value = data.get('Temperature')['value']
        self.Temperature_unit = data.get('Temperature')['unit']

        self.Pressure_value = data.get('Pressure')['value']
        self.Pressure_unit = data.get('Pressure')['unit']

        self.Rainfall_value = data.get('Rainfall')['value']
        self.Rainfall_unit = data.get('Rainfall')['unit']

        self.Wind_velocity_value = data.get('Wind velocity')['value']
        self.Wind_velocity_unit = data.get('Wind velocity')['unit']

        self.Humidity_value = data.get('Humidity')['value']
        self.Humidity_unit = data.get('Humidity')['unit']

        self.Date_value = data.get('Date')['value']
        self.Date_unit = data.get('Date')['unit']

        self.Hour_value = data.get('Hour')['value']
        self.Hour_unit = data.get('Hour')['unit']

    def __str__(self):
        return (
            f"City: {self.City}\n"
            f"Temperature: {self.Temperature_value} {self.Temperature_unit}\n"
            f"Pressure: {self.Pressure_value} {self.Pressure_unit}\n"
            f"Rainfall: {self.Rainfall_value} {self.Rainfall_unit}\n"
            f"Wind Velocity: {self.Wind_velocity_value} {self.Wind_velocity_unit}\n"
            f"Humidity: {self.Humidity_value} {self.Humidity_unit}\n"
            f"Date: {self.Date_value} {self.Date_unit}\n"
            f"Hour: {self.Hour_value} {self.Hour_unit}"
        )


polish_weather = PolishWeather()
temp = polish_weather.get_formatted_city_data('warszawa')
weather = Weather(temp)
print(weather)