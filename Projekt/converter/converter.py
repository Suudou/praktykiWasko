from .Velocity import convert_velocity
from .temperature import convert_temperature


class Converter:
    def convert(unit_type: str, dst: str, val: float, src: str):
        match unit_type:
            case "temperature": return convert_temperature(dst, val, src)
            case "wind_velocity": return convert_velocity(dst, val, src)
