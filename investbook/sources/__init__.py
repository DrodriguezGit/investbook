from investbook.sources.polygon import PolygonAPI

class AssetsAPI:

    def __init__(self, polygon_api_key: str, avantage_api_key:str) -> None:
        self._polygon_api_key = polygon_api_key
        self._avantage_api_key = avantage_api_key

    @property
    def polygon(self):
        return PolygonAPI(self._polygon_api_key)
    
    @property
    def alphavantage(self):
        return None