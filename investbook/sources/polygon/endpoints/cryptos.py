from ..base import PolygonQueryManager


class PolygonEndpointCrypto(PolygonQueryManager):

    def get_price(self, ticker: str, currency: str, date: str) -> dict:
        '''
        https://polygon.io/docs/crypto/get_v1_open-close_crypto__from___to___date
        '''
        return self.get(f'/v1/open-close/crypto/{ticker}/{currency}/{date}')