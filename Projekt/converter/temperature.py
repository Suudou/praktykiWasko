

def convert_temperature(dst, val, src='C'):
    def source_to_celsius(value, source):
        match source:
            case 'C':
                return value
            case 'K':
                return value - 273.15
            case 'F':
                return (value - 32) * 5/9
    temp_celsius = source_to_celsius(val, src)
    match dst:
        case 'C':
            return val
        case 'K':
            return round(temp_celsius + 273.15)
        case 'F':
            return round((temp_celsius * 9 / 5) + 32)
        case _:
            raise ValueError(f"Nieobsługiwana jednostka temperatury: {dst}")
