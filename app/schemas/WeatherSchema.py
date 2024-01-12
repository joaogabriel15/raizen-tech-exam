from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class Coordinates(BaseModel):
    lat: Optional[float] = None
    lon: Optional[float] = None

class Query(BaseModel):
    city_name: Optional[str] = None
    state_code: Optional[int] = None
    coutry_code: Optional[int] = None

class TypeSearch(str, Enum):
    coordinates = 'coordinates'
    query = 'query'
    id = 'id'

class WeatherRequest(BaseModel):
    type_search: TypeSearch 
    coordinates:Coordinates = None
    query: Query = None
    city_id: Optional[int] = None
   

class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str

class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    sea_level: int
    grnd_level: int
    humidity: int
    temp_kf: float

class Clouds(BaseModel):
    all: int

class Wind(BaseModel):
    speed: float
    deg: int
    gust: Optional[float]

class Sys(BaseModel):
    pod: str

class Forecast(BaseModel):
    dt: int
    main: Main
    weather: List[Weather]
    clouds: Clouds
    wind: Wind
    visibility: int
    pop: int
    sys: Sys
    dt_txt: str

class WeatherResponse(BaseModel):
    cod: str
    message: int
    cnt: int
    list: List[Forecast]
    timestamp: datetime