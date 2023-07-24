"""
def convert_temperature(dst, val, src='C'):
    if src == dst:
        return val
    if src != 'C' and dst != 'C':
        auxiliary_value = convert_temperature('C', val, src)
        return convert_temperature(dst, auxiliary_value, 'C')
    if dst == 'C':
        match src:
            case 'F':
                return (val - 32) * 5/9
            case 'K':
                return val - 273
    elif src == 'C':
        match dst:
            case 'F':
                return (val * 9/5) + 32
            case 'K':
                return val + 273
    else:
        raise ValueError("Błąd" + src)"""

#druga wersja Funkcji konwertującej temperature, rekurencja zastąpiona funkcją zanieżdżoną
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
