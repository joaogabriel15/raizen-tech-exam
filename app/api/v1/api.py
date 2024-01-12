from fastapi import APIRouter, Response, status, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.WeatherSchema import WeatherRequest
from app.controllers.weather_controller import get_weather_api, get_weather_local

api = APIRouter(prefix="/api/v1")


@api.post('/search')
def search_wather(data:WeatherRequest = None) -> Response:
    """
    Rota para buscar informações meteorológicas da API OpenWeatherMap.

    Parâmetros:
    - data (WeatherRequest): Dados de requisição contendo os parâmetros de busca.

    Retorna:
    - Response: Resposta JSON contendo informações meteorológicas.

    Exemplo de Uso:
    - POST /api/v1/search/  json={"type_search": "coordinates", "coordinates": {"lat": 40.7128, "lon": -74.0060}}
    """
    
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='missing or incorrect parameters'
        )
     
    res = get_weather_api(data)

    return JSONResponse(
     content=res,
     status_code=status.HTTP_200_OK
    )

@api.get('/search/local')
def search_wather(skip: int = 0, limit: int = 10) -> Response:
    """
    Rota para buscar informações meteorológicas locais armazenadas no banco de dados.

    Parâmetros:
    - skip (int): Número de documentos a serem ignorados antes de começar a recuperar dados.
    - limit (int): Número máximo de documentos a serem recuperados.

    Retorna:
    - Response: Resposta JSON contendo informações meteorológicas locais.

    Exemplo de Uso:
    - GET /api/v1/search/local?skip=0&limit=10
    """
    res = get_weather_local(skip,limit)

    return Response(
     content=res,
     status_code=status.HTTP_200_OK
    )