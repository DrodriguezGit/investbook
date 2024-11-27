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


# ENDPOINT

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
    
    def info(self, ticker: str): 
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
        return self.get(f'/api/v3/quote/{ticker}')

    
    
