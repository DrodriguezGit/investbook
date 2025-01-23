from __future__ import annotations
from typing import Optional
from pydantic import BaseModel

from investbook.sources.fmp.base import FMPQueryManager

# MODELOS

class Stock(BaseModel):
    exchange: Optional[str]
    exchangeShortName: Optional[str]
    name: Optional[str]
    price: Optional[float]
    symbol: Optional[str]
    type: Optional[str]
    
class Stock_Info(BaseModel):
    symbol: str
    exchangeShortName: Optional[str] = None  
    type: Optional[str] = None  
    name: Optional[str] = None
    price: Optional[float] = None
    changesPercentage: Optional[float] = None
    dayLow: Optional[float] = None
    dayHigh: Optional[float] = None
    yearHigh: Optional[float] = None
    yearLow: Optional[float] = None
    marketCap: Optional[int] = None
    priceAvg50: Optional[float] = None
    priceAvg200: Optional[float] = None
    volume: Optional[int] = None
    timestamp: Optional[int] = None



class FmpStock(FMPQueryManager):
        
    def list(self, type: str='stock') -> list[Stock]:
        """
        https://site.financialmodelingprep.com/developer/docs#symbol-list-stock-list

        Ticker stock companies
        -
        Devuelve una lista de los tickers, el exchange y el nombre de las empresas


        Returns
        -
            list of Stock
        """
        
        return [Stock.model_validate(r) for r in self.get(f'/api/v3/{type}/list')]
    
    def info(self, ticker: str) -> list[Stock_Info]: 
        """
        https://site.financialmodelingprep.com/developer/docs#full-quote-quote

        Company names 
        -
        Devuelve información de mercado de la empresa
        
        Params
        -
         :param ticker (str)

        Returns
        -
            list of dictionaries

        """
        return [Stock_Info.model_validate(r) for r in self.get(f'/api/v3/quote/{ticker}')]

    
    
