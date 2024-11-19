from investbook.sources.polygon import PolygonAPI

class DataSources:

    def __init__(self, polygon_api_key: str, avantage_api_key:str) -> None:
        self.polygon_api_key = polygon_api_key
        self.avantage_api_key = avantage_api_key

    @property
    def polygon(self):
        return PolygonAPI(self.polygon_api_key)
    
    @property
    def alphavantage(self):
        return None