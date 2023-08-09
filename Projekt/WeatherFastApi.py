from fastapi import FastAPI, Path, Request, Query
import jinja2
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
from starlette.responses import JSONResponse

from weather.countries.germany import GermanyWeather
from weather.countries.polish import PolishWeather
from weather.baseWeather import URLTemplate
from weather.countries import polish, germany
polish_weather = PolishWeather()
german_weather = GermanyWeather()


app = FastAPI()


@app.get("/weather/{country}/cities")
def get_cities_for_country(country: str):
    if country.lower() == 'poland':
        cities = polish_weather.get_city_names()
    elif country.lower() == 'germany':
        cities = german_weather.get_city_names()
    else:
        return JSONResponse(content={"error": "Invalid country"}, status_code=400)
    return cities


# Todo:
#  w osobnym pliku @app.get("/converter") query paramsy to co wchodzi do funkcji




"""
app = FastAPI()

# nowy html
# @app.get("index/, response_class=HTMLResponse")


@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    cities = CityChoice.cities_get()
    return templates.TemplateResponse("index.html", {"request": request, "cities": cities})


@app.get("/get-by-station")
def get_station(name: str):
    cities = CityChoice.cities_get()
    name = name.capitalize()
    if name in cities:
        city = CityChoice.chosen_city(name)
        return city
    return "station not found"


templates = Jinja2Templates(directory="templates")


"""