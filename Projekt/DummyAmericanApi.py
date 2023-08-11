"""
Dummy endpoints to use as weather source
"""
from fastapi import APIRouter
import random as rd
import datetime as dt
import json

router = APIRouter()


@router.get("/us/{year}/{month}/{day}")
async def read_users(year: int, month: int, day: int, hour: str = "0AM"):
    try:
        hour_24h: int = int(hour[:-2]) if hour[-2] == 'A' else (int(hour[:-2]) + 12)%12
        date: dt.datetime = dt.datetime.fromisoformat(f"{year}-{month:02}-{day:02}T{hour_24h:02}:00:00")
    except:
        return {"ERROR": "Usage: /us/yyyy/MM/dd?hour=hh, where hh is in 12hour format (AM/PM)"}
    cities = [
        ("NY", "New York"),
        ("CA", "Los Angeles"),
        ("IL", "Chicago"),
        ("TX", "Houston"),
        ("AZ", "Phoenix"),
        ("PA", "Philadelphia"),
        ("TX", "San Antonio"),
        ("CA", "San Diego"),
        ("TX", "Dallas"),
        ("CA", "San Jose"),
        ("TX", "Austin"),
        ("IN", "Indianapolis"),
        ("FL", "Jacksonville"),
        ("TX", "Fort Worth"),
        ("OH", "Columbus"),
        ("TN", "Nashville"),
        ("NC", "Charlotte"),
        ("AZ", "Tucson"),
        ("OK", "Oklahoma City"),
        ("CO", "Denver"),
        ("MA", "Boston"),
        ("WA", "Seattle"),
        ("DC", "Washington"),
        ("TN", "Memphis"),
        ("MD", "Baltimore"),
        ("KY", "Louisville"),
        ("OR", "Portland"),
        ("NV", "Las Vegas"),
        ("WI", "Milwaukee")
    ]
    return json.loads(json.dumps([generate_random_city_data(state, city, date) for state, city in cities]))


def generate_random_city_data(state: str, city: str, date: dt.datetime) -> dict:
    rd.seed(sum([ord(x) for x in state.lower() + city.lower() + str(date)]))
    return {
        "location": {
            "state": state,
            "city": city
        },
        "time": {
            "date": str(date.date()),
            "time": str(date.time())
        },
        "weather": {
            "temperature": f"{rd.uniform(20,100):.2f}F",
            "humidity": f"{rd.randint(0,100)}.{rd.randint(0,9)}%",
            "pressure": f"{rd.randint(980,1050)}mb",
            "wind_speed": f"{rd.randint(0,50)}mph",
            "rainfall": f"{rd.uniform(0,10):.2f}in"
        }
    }
