import temperature
import Velocity


class Converter:
    def convert(unit_type: str, dst: str, val: float, src: str):
        match unit_type:
            case "temperature": return temperature.convert_temperature(dst, val, src)
            case "wind_velocity": return Velocity.convert_velocity(dst, val, src)
