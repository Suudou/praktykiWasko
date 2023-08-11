from fastapi import FastAPI, Path, Request, Query
import jinja2
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
from starlette.responses import JSONResponse
import DummyAmericanApi
import ConverterFastApi
from weather.countries.germany import GermanyWeather
from weather.countries.poland import PolishWeather
from weather.baseWeather import URLTemplate
from weather.countries import poland, germany
from weather.countries.america import AmericanWeather


polish_weather = PolishWeather()
german_weather = GermanyWeather()
american_weather = AmericanWeather()

app = FastAPI()
app.include_router(ConverterFastApi.converter_app_router)
app.include_router(DummyAmericanApi.router)


@app.get("/weather/{country}/cities")
def get_cities_for_country(country: str):
    if country.lower() == 'poland':
        cities = polish_weather.get_city_names()
    elif country.lower() == 'germany':
        cities = german_weather.get_city_names()
    elif country.lower() == 'america':
        cities = american_weather.get_city_names()
    else:
        return JSONResponse(content={"error": "Invalid country"}, status_code=400)
    return cities


@app.get("/weather/{country}/{city}/forecast")
def get_weather_forecast_for_city(
    country: str,
    city: str = Path(..., title="City", description="Chose city")
):
    if country.lower() == 'poland':
        city_weather_data = polish_weather.get_formatted_city_data(city)
    elif country.lower() == 'germany':
        city_weather_data = german_weather.get_formatted_city_data(city)
    elif country.lower() == 'america':
        city_weather_data = american_weather.get_formatted_city_data(city)
    else:
        return JSONResponse(content={"error": "Invalid country"}, status_code=400)
    return city_weather_data


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
# Todo:
#  w osobnym pliku @app.get("/converter") query paramsy to co wchodzi do funkcji
#  templates = Jinja2Templates(directory="templates")
