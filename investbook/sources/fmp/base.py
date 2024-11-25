import requests as rq
from urllib.parse import urlencode, urlunsplit, quote_plus
from pprint import pprint

class FMPQueryManager:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = 'financialmodelingprep.com/api'
        self.session = rq.Session()

    @property
    def headers(self) -> dict:
        return {
            'Accept': "application/json",
            'Content-Type': "application/json",
        }

    def url_maker(self, base_url: str, endpoint: str, params: dict = None) -> str:

        if params is None:
            params = {}
        params["apikey"] = self.api_key

        encoded_params = {quote_plus(k): quote_plus(str(v)) for k, v in params.items() if v}
        query = urlencode(encoded_params, doseq=True)
        
        return urlunsplit(("https", base_url, endpoint, query or "", ""))

    def get(self, endpoint: str, **params) -> dict:
        try:
            url = self.url_maker(self.base_url, endpoint, params)
            
            response = self.session.get(url, headers=self.headers)
            response.raise_for_status()
            
            return response.json()
        except rq.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
            raise
        except rq.exceptions.ConnectionError as e:
            print(f"Connection Error: {e}")
            raise
        except Exception as e:
            print(f"Unexpected Error: {e}")
            raise
