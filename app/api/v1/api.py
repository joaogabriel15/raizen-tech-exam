from fastapi import APIRouter, Response, status
from fastapi.responses import JSONResponse
from app.schemas.WeatherSchema import WeatherRequest
from app.controllers.weather_controller import get_weather_api, get_weather_local

api = APIRouter(prefix="/api/v1")


@api.get('/search')
def search_wather(data:WeatherRequest = None) -> Response:
    res = get_weather_api(data)

    return JSONResponse(
     content=res,
     status_code=status.HTTP_200_OK
    )

@api.get('/search/local')
def search_wather(skip: int = 0, limit: int = 10) -> Response:
    res = get_weather_local(skip,limit)

    return Response(
     content=res,
     status_code=status.HTTP_200_OK
    )