from investbook.sources.polygon import PolygonAPI
from investbook.sources.fmp import FMPAPI

class AssetsAPI:

    def __init__(self, polygon_api_key: str, fmp_api_key:str) -> None:
        self._polygon_api_key = polygon_api_key
        self._fmp_api_key = fmp_api_key

    @property
    def polygon(self):
        return PolygonAPI(self._polygon_api_key)
    
    @property
    def fmp(self):
        return FMPAPI(self._fmp_api_key)