from ..base import PolygonQueryManager


class PolygonEndpointCrypto(PolygonQueryManager):

    def get_price(self, ticker: str, currency: str, date: str) -> dict:
        """
        https://polygon.io/docs/crypto/get_v1_open-close_crypto__from___to___date
                    
        Ticker crypto prices
        -
        Devuelve el precio de los tickers disponibles de criptmonedas

        Params
        -
        :param ticker (str): tipo de activo. Consultar `.get_tickers`
        :param currency (str): EUR | USD
        :param date (str): (yyyy-mm-dd)

        Returns
        -
            list of dictionaries
        """
        return self.get(f'/v1/open-close/crypto/{ticker}/{currency}/{date}')