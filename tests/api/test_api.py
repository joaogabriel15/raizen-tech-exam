import pytest, requests as rq
from os import getenv
from dotenv import load_dotenv, dotenv_values

load_dotenv()

class TestApi:
    api_key = getenv('API_KEY')
    lang    = 'pt_br'
    api_url = 'api.openweathermap.org'
    units   = 'metric'

    def test_request(self):
        r = rq.get(f" https://{self.api_url}/data/2.5/forecast?lat=44.34&lon=10.99&lang={self.lang}&units={self.units}&appid={self.api_key}")
        print(r.json())
        