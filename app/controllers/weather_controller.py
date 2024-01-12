from fastapi import HTTPException, status
from datetime import datetime
from requests import get
from os import getenv
from app.schemas.WeatherSchema import WeatherRequest, WeatherResponse, TypeSearch
from app.database import colletion


def get_weather_api(data: WeatherRequest):
    _lang    = 'pt_br'
    _units   = 'metric'
    _api_key = getenv('API_KEY')
    _api_url = 'api.openweathermap.org'

    type_search, \
    coordinates, \
    query, \
    city_id= data.model_dump().values()


    if type_search is TypeSearch.coordinates :
        response = get(f"https://{_api_url}/data/2.5/forecast?lat={coordinates.lat}&lon={coordinates.lon}&lang={_lang}&units={_units }&appid={_api_key}")

        document: WeatherResponse = response.json()
        document['timestamp'] = datetime.now().timestamp()
        colletion.insert_one(document)
        
        return response.json()
    
    if type_search is TypeSearch.query :
        q = []

        for params in query:
            if params is not None:
                q.append(params)

        response = get(f"https://{_api_url}/data/2.5/forecast?q={','.join(q)}&lang={_lang}&units={_units }&appid={_api_key}")
        
        document: WeatherResponse = response.json()
        document['timestamp'] = datetime.now().timestamp()
        colletion.insert_one(document)

        return response.json()
    
    if type_search is TypeSearch.id :
        response = get(f"https://{_api_url}/data/2.5/forecast?id={city_id}&lang={_lang}&units={_units }&appid={_api_key}")
        
        document: WeatherResponse = response.json()
        document['timestamp'] = datetime.now().timestamp()
        colletion.insert_one(document)
        
        return response.json()

    
    raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect or missing parameters.'
        )

def get_weather_local():
    pass