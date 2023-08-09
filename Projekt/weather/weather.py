
class Weather:
    def __init__(self, data: dict):
        self.data = {}
        units = {
            'Temperature': 'C',
            'Pressure': 'hPa',
            'Rainfall': 'mm',
            'Wind velocity': 'km/h',
            'Humidity': '%',
            'Hour': 'CEST'
        }
        for key, value in data.items():
            if key in units:
                self.data[key] = {'value': value, 'unit': units[key]}
            else:
                self.data[key] = value

    def __str__(self):
        return str(self.data)


