from fastapi import FastAPI, Path, Request
import CityChoice
import jinja2
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn


app = FastAPI()


#@app.get("index/, response_class=HTMLResponse")



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


