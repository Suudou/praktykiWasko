
def convert_velocity(dst, val, src='kilometers_per_hour') -> int:
    def source_to_kmh(value, source):
        match source:
            case 'kilometers_per_hour':
                return value
            case 'meters_per_second':
                return value * 3.6
            case 'miles_per_hour':
                return value * 1.61
    temp_kmph = source_to_kmh(val, src)
    match dst:
        case 'kilometers_per_hour':
            return temp_kmph
        case 'meters_per_second':
            return round(temp_kmph / 3.6)
        case 'miles_per_hour':
            return round((temp_kmph / 1.61))
        case _:
            raise ValueError(f"unit not supported: {dst}")
