from ..base import PolygonQueryManager


class PolygonEndpointIndex(PolygonQueryManager):

    def get_price(self, ticker: str, date: str) -> dict:
            '''
            https://polygon.io/docs/indices/get_v1_open-close__indicesticker___date
            '''
            return self.get(f'/v1/open-close/{ticker}/{date}')