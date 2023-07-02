from fastapi import FastAPI, Path, Request
import CityChoice
import jinja2
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import uvicorn

app = FastAPI()

@app.get("/home")
def home():
    return weather

#@app.get("index/, response_class=HTMLResponse")

@app.get("/get-by-station")
def get_station(name: str):
    cities = CityChoice.cities_get()
    name = name.capitalize()
    if name in cities:
        city = CityChoice.chosen_city(name)
        return city
    return "station not found"





#@app.post("/weather/{station}")
#def station(item: Station)

testname = "krakow"
weather = CityChoice.chosen_city(testname)


# weather = Weather(chosen_city(formatted_in))

