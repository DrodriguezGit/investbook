from investbook.sources.polygon.base import PolygonQueryManager


class PolygonEndpointIndex(PolygonQueryManager):

    def get_price(self, ticker: str, date: str) -> dict:
        """
        https://polygon.io/docs/indices/get_v1_open-close__indicesticker___date
            
        Ticker indices prices
        -
        Devuelve el precio de los tickers disponibles de indices

        Params
        -
        :param ticker (str): tipo de activo. Consultar `.get_tickers`
        :param date (str): (yyyy-mm-dd)

        Returns
        -
            list of dictionaries
        """
        return self.get(f'/v1/open-close/{ticker}/{date}')