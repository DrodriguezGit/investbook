from ..base import PolygonQueryManager


class PolygonEndpointInfo(PolygonQueryManager):


    def get_ticker_types(self, asset_class: str) -> list[dict]:
        """
        https://polygon.io/docs/stocks/get_v3_reference_tickers_types

        Ticker types
        -
        Devuelve los tipos de ticker disponibles

        Params
        -
        :param asset_class: stocks | options | crypto | fx | indices

        Returns
        -
            list of dictionaries
        """
        return self.get('/v3/reference/tickers/types', asset_class=asset_class)

    def get_tickers(
            self,
            market: str='stocks',
            type: str='CS',
            search: str=None,
            limit: int=100
        ) -> list[dict]:
        """
        https://polygon.io/docs/stocks/get_v3_reference_tickers
        
        Tickers
        -
        Devuelve los tipos de tickers disponibles

        Params
        -
        :param market (str): ["stocks", "otc", "crypto", "fx", "indices"]
        :param type (str): tipo de activo. Consultar `.get_ticker_types`

        Returns
        -
            list of dictionaries
        """
        return self.get(
            '/v3/reference/tickers/',
            market=market,
            type=type,
            search=search,
            limit=limit
        )