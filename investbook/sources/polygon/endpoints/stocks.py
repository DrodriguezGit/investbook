from __future__ import annotations
from ..base import PolygonQueryManager
from typing import Optional, List
from pydantic import BaseModel, root_validator

class StockPrice(BaseModel):
    symbol: Optional[str]
    date: Optional[str]  # Usamos 'date' en vez de 'from'
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    close: Optional[float]
    volume: Optional[int]
    afterHours: Optional[float]
    preMarket: Optional[float]
    
    @root_validator(pre=True)
    def clean_data(cls, values):
        # Limpiamos el campo 'status' y renombramos 'from' a 'date'
        if 'status' in values:
            del values['status']
        if 'from' in values:
            values['date'] = values.pop('from') 
        return values

class PolygonEndpointStocks(PolygonQueryManager):
    
    def get_price(self, ticker: str, date: str) -> StockPrice:
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
        return StockPrice.model_validate(self.get(f'/v1/open-close/{ticker}/{date}'))  
 