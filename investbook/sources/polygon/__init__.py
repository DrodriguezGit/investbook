import requests as rq
from urllib.parse import (
    quote_plus,
    urlencode,
    urlunsplit
)
from investbook.sources.shared import QueryManager

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
            params = {quote_plus(k) : quote_plus(v) for k, v in params.items()}

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


class PolygonAPI(PolygonQueryManager):

    def get_tickers(self,market: str, type: str, search: str) -> dict: #Pilla los tickets de todos los tipos de activos
        '''
        https://polygon.io/docs/stocks/get_v3_reference_tickers
        '''
        return self.get('/v3/reference/tickers/', market = market, type=type, search=search)
    
    def get_price_stock(self, ticker: str, date: str) -> dict:
        '''
        https://polygon.io/docs/stocks/get_v1_open-close__stocksticker___date
        '''
        return self.get(f'/v1/open-close/{ticker}/{date}')
    
    def get_option_contract(self, underlying_ticker: str) -> dict:
        
        return self.get(f'v3/reference/options/contracts/{underlying_ticker}')
    
    def get_price_option(self, optionsTicker: str, date: str) -> dict:
        '''
        https://polygon.io/docs/options/get_v1_open-close__optionsticker___date
        '''
        return self.get(f'/v1/open-close/{optionsTicker}/{date}')
    
    def get_price_indice(self, indicesTicker: str, date: str) -> dict:
        '''
        https://polygon.io/docs/indices/get_v1_open-close__indicesticker___date
        '''
        return self.get(f'/v1/open-close/{indicesTicker}/{date}')
    
    def get_price_crypto(self, crypto: str, currency: str, date: str) -> dict:
        '''
        https://polygon.io/docs/crypto/get_v1_open-close_crypto__from___to___date
        '''
        return self.get(f'/v1/open-close/crypto/{crypto}/{currency}/{date}')
