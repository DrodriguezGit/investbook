from investbook.sources.polygon import PolygonAPI
from investbook.sources.fmp import FMPAPI
from investbook.sources.finhub import FINHUBAPI
from investbook.sources.yfinance.init import YfinanceAPI

class AssetsAPI:

    def __init__(self, polygon_api_key: str=None, fmp_api_key:str=None, finhub_api_key:str=None) -> None:
        self._polygon_api_key = polygon_api_key
        self._fmp_api_key = fmp_api_key
        self._finhub_api_key = finhub_api_key

    @property
    def polygon(self):
        return PolygonAPI(self._polygon_api_key)
    
    @property
    def fmp(self):
        return FMPAPI(self._fmp_api_key)
    
    @property
    def finhub(self):
        return FINHUBAPI(self._finhub_api_key)
    
    @property
    def yfinance(self):
        return YfinanceAPI()