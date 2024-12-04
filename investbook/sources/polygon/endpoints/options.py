from ..base import PolygonQueryManager
from __future__ import annotations
from typing import Optional, List
from pydantic import BaseModel


class OptionPrice(BaseModel):
    symbol: str
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    afterHours: float
    preMarket: float


class PolygonEndpointOption(PolygonQueryManager):
    
    def get_price(self, option_ticker: str, date: str) -> OptionPrice:
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
        return [OptionPrice.model_validate (r) for r in self.get(f'/v1/open-close/{option_ticker}/{date}')]