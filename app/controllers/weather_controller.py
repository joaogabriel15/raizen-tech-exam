from fastapi import HTTPException, status
from datetime import datetime
from bson import json_util
from requests import get
from os import getenv
from app.schemas.WeatherSchema import WeatherRequest, WeatherResponse, TypeSearch
from app.database import colletion


def get_weather_api(data: WeatherRequest):
    """
    Recupera informações meteorológicas da API OpenWeatherMap com base nos dados fornecidos.

    Parâmetros:
    - data (WeatherRequest): Uma instância do modelo WeatherRequest contendo parâmetros de pesquisa.

    Retorna:
    - dict: Resposta JSON contendo informações meteorológicas.

    Levanta:
    - HTTPException: Em caso de códigos de status HTTP 404 (Not Found) ou 400 (Bad Request).

    Exemplo de Uso:
    ```python
    dados_climaticos = WeatherRequest(...)  # Inicialize WeatherRequest com parâmetros apropriados.
    resultado = get_weather_api(dados_climaticos)
    ```
    """

    _lang    = 'pt_br'
    _units   = 'metric'
    _api_key = getenv('API_KEY')
    _api_url = 'api.openweathermap.org'

    type_search, \
    coordinates, \
    query, \
    city_id= data.model_dump().values()



    if type_search is TypeSearch.coordinates :
        """
        Recupera informações meteorológicas usando coordenadas.

        Parâmetros:
        - coordinates (Coordinates): Objeto contendo latitude e longitude.

        Retorna:
        - dict: Resposta JSON contendo informações meteorológicas para as coordenadas especificadas.
        """

        response = get(f"https://{_api_url}/data/2.5/forecast?lat={coordinates['lat']}&lon={coordinates['lon']}&lang={_lang}&units={_units }&appid={_api_key}")

        if response.status_code == 404:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Not found.'
            )
        
        document: WeatherResponse = response.json()
        document['timestamp'] = datetime.now().timestamp()
        colletion.insert_one(document)
        
        return response.json()
    
    if type_search is TypeSearch.query :
        """
        Recupera informações meteorológicas usando uma consulta.

        Parâmetros:
        - query (list): Lista de parâmetros para a consulta.

        Retorna:
        - dict: Resposta JSON contendo informações meteorológicas para a consulta especificada.
        """

        q = []

        print(query)
        for params in query:
            if query[params] is not None:
                q.append(query[params])
        print(f"https://{_api_url}/data/2.5/forecast?q={','.join(q) if len(q) > 1 else q[0]}&lang={_lang}&units={_units }&appid={_api_key}")

        response = get(f"https://{_api_url}/data/2.5/forecast?q={','.join(q) if len(q) > 1 else q[0]}&lang={_lang}&units={_units }&appid={_api_key}")
        
        if response.status_code == 404:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Not found.'
            )

        document: WeatherResponse = response.json()
        document['timestamp'] = datetime.now().timestamp()
        colletion.insert_one(document)

        return response.json()
    
    if type_search is TypeSearch.id :
        """
        Recupera informações meteorológicas usando um ID de cidade.

        Parâmetros:
        - city_id (int): O ID da cidade.

        Retorna:
        - dict: Resposta JSON contendo informações meteorológicas para o ID da cidade especificado.
        """

        response = get(f"https://{_api_url}/data/2.5/forecast?id={city_id}&lang={_lang}&units={_units }&appid={_api_key}")
        

        if response.status_code == 404:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Not found.'
            )

        document: WeatherResponse = response.json()
        document['timestamp'] = datetime.now().timestamp()
        colletion.insert_one(document)
        
        return response.json()

    
    raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect or missing parameters.'
        )



def get_weather_local(skip:int, limit:int):
    """
    Recupera informações meteorológicas locais armazenadas no banco de dados.

    Parâmetros:
    - skip (int): O número de documentos a serem ignorados antes de começar a recuperar dados.
    - limit (int): O número máximo de documentos a serem recuperados.

    Retorna:
    - str: Representação JSON dos documentos meteorológicos recuperados.

    Exemplo de Uso:
    ```python
    resultado_json = get_weather_local(0, 10)  # Recupera os primeiros 10 documentos meteorológicos.
    ```
    """
    cursor = colletion.find({}).skip(skip).limit(limit)
    documents = list(cursor)
    json_data = json_util.dumps(documents, default=json_util.default, indent=2)


    return json_data
