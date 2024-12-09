from ..base import PolygonQueryManager
from typing import List, Optional
from pydantic import BaseModel

class Ticker(BaseModel):
    ticker: str
    name: str
    market: str
    locale: str
    primary_exchange: Optional[str] 
    type: str
    active: bool
    currency_name: Optional[str]
    cik: Optional[str] = None
    composite_figi: Optional[str] = None
    share_class_figi: Optional[str] = None
    last_updated_utc: Optional[str] = None


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
            self, ticker:str, market: str='stocks', type: str='CS', search: str=None, limit: int=100) -> Ticker:
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
        response_data = self.get('/v3/reference/tickers/', ticker=ticker, market=market, type=type, search=search, limit=limit)
    
    # Extrae la lista de resultados y valida cada uno
        results = response_data.get("results", [])
        return [Ticker.model_validate(item) for item in results]

        # return Ticker.model_validate(self.get('/v3/reference/tickers/', market=market, type=type, search=search, limit=limit).get("results", []))