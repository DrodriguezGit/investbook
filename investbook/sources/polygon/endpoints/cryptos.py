from __future__ import annotations
from ..base import PolygonQueryManager
from typing import List
from pydantic import BaseModel

class Trade(BaseModel):
    x: int  
    p: float  
    s: float  
    c: List[int]  
    i: str  
    t: int  

class PolygonCryptoPrice(BaseModel):
    symbol: str  
    isUTC: bool 
    day: str  
    open: float  
    close: float  
    openTrades: List[Trade]  
    closingTrades: List[Trade]  

class PolygonEndpointCrypto(PolygonQueryManager):

    def get_price(self, ticker: str, currency: str, date: str) -> PolygonCryptoPrice:
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
        return PolygonCryptoPrice.model_validate(self.get(f'/v1/open-close/crypto/{ticker}/{currency}/{date}'))