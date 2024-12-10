from __future__ import annotations
from investbook.sources.polygon.base import PolygonQueryManager
from typing import Optional
from pydantic import BaseModel

class PolygonIndexPrice(BaseModel):
    status: Optional[str]
    symbol: Optional[str]
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    close: Optional[float]
    afterHours: Optional[float]
    preMarket: Optional[float]
    

class PolygonEndpointIndex(PolygonQueryManager):

    def get_price(self, ticker: str, date: str) -> PolygonIndexPrice:
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
        return PolygonIndexPrice.model_validate(self.get(f'/v1/open-close/{ticker}/{date}'))