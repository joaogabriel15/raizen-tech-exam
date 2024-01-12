from fastapi.testclient import TestClient
from app.main import app, load_dotenv
from json import dumps
from app.schemas.WeatherSchema import WeatherRequest, TypeSearch


load_dotenv()
client = TestClient(app)


def test_no_params_weather_api_coordinates():
    res  = client.post('/api/v1/search/')

    assert res.status_code == 400
    assert dict(res.json())['detail'] == "missing or incorrect parameters"


def test_get_weather_api_coordinates():
    mock_params:WeatherRequest = {
        "type_search" : TypeSearch.coordinates,
        "coordinates" : {
            "lon":10.99,
            "lat":44.34
        }
    }

    res  = client.post('/api/v1/search', json=mock_params, headers={'Content-Type':'application/json'})

    assert res.status_code == 200
    assert res.headers['Content-Type'] == 'application/json'
    res.close()

def test_get_weather_api_query():
    mock_params:WeatherRequest = {
        "type_search" : TypeSearch.query,
        "query" : {
            "city_name":"London",
            "country_code":"US"
        }
    }

    res  = client.post('/api/v1/search', json=mock_params, headers={'Content-Type':'application/json'})

    assert res.status_code == 200
    assert res.headers['Content-Type'] == 'application/json'
    res.close()


def test_get_weather_api_id():
    mock_params:WeatherRequest = {
        "type_search" : TypeSearch.id,
        "city_id" : 2960
    }

    res  = client.post('/api/v1/search', json=mock_params, headers={'Content-Type':'application/json'})

    assert res.status_code == 200
    assert res.headers['Content-Type'] == 'application/json'
    res.close()

    



