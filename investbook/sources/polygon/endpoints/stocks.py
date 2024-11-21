from ..base import PolygonQueryManager


class PolygonEndpointStocks(PolygonQueryManager):
    
    def get_price(self, ticker: str, date: str) -> dict:
        '''
        https://polygon.io/docs/stocks/get_v1_open-close__stocksticker___date
        '''
        return self.get(f'/v1/open-close/{ticker}/{date}')