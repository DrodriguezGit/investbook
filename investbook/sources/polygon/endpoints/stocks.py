from ..base import PolygonQueryManager


class PolygonEndpointStocks(PolygonQueryManager):
    
    def get_price(self, ticker: str, date: str) -> dict:
        """
        https://polygon.io/docs/stocks/get_v1_open-close__stocksticker___date            
        
        Ticker stocks prices
        -
        Devuelve el precio de los tickers disponibles de stocks

        Params
        -
        :param ticker (str): tipo de activo. Consultar `.get_tickers`
        :param date (str): (yyyy-mm-dd)

        Returns
        -
            list of dictionaries
        """
        return self.get(f'/v1/open-close/{ticker}/{date}')