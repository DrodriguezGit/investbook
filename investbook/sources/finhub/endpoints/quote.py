from __future__ import annotations
from investbook.sources.finhub.base import FinHubQueryManager
from typing import Optional, List
from pydantic import BaseModel



class FinHubQuoteData(BaseModel):
    c: float  
    h: float  
    l: float  
    o: float  
    pc: float 


class FinHubQuote(FinHubQueryManager):
    
    def get_cuote(self, symbol: str) -> FinHubQuoteData:
        """
        https://finnhub.io/docs/api/quote
        
        -
        Obtiene datos de cotización en tiempo real de acciones estadounidenses.
        
        :param symbol (str): El ticker de la empresa que busques
        
        return: Devuelve una lista con los datos de cotización de apertura, cierre, valor más alto, valor más bajo y precio de cierre del dia anterior
        
        """
        return FinHubQuoteData.model_validate(self.get('/quote', symbol=symbol)) 