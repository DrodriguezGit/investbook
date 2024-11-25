from ..base import PolygonQueryManager


class PolygonEndpointOption(PolygonQueryManager):
    
    def get_price(self, option_ticker: str, date: str) -> dict:
        """
        https://polygon.io/docs/options/get_v1_open-close__optionsticker___date
                    
        Ticker option prices
        -
        Devuelve el precio de los tickers disponibles de opciones

        Params
        -
        :param option_ticker (str): tipo de activo. Consultar `.get_tickers`
        :param date (str): (yyyy-mm-dd)

        Returns
        -
            list of dictionaries
        """
        return self.get(f'/v1/open-close/{option_ticker}/{date}')