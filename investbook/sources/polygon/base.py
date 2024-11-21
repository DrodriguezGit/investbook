import requests as rq
from urllib.parse import (
    quote_plus,
    urlencode,
    urlunsplit
)

class PolygonQueryManager:

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = 'api.polygon.io'
        self.session = rq.Session()
    
    @property
    def headers(self) -> dict:
        return {
            'Accept': "application/json",
            'Content-Type': "application/json",
            'Authorization': f"Bearer {self.api_key}"
        }

    def url_maker(self, url: str, endpoint: str, params: dict=None) -> str:
        
        if params:
            params = {quote_plus(k) : quote_plus(str(v)) for k, v in params.items() if v}

        query = urlencode(query=params or "", doseq=True)
        
        return urlunsplit(("https", url, endpoint, query or "", ""))
    
    def get(self, endpoint: str, **params) -> dict:

        try:
            url = self.url_maker(self.base_url, endpoint, params)

            r = self.session.get(url, headers=self.headers)
            
            r.raise_for_status()

            response: dict = r.json()

            return response

        except rq.HTTPError as e:

            print(e)
