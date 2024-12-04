from __future__ import annotations
from typing import Optional, List
from pydantic import BaseModel

from investbook.sources.fmp.base import FMPQueryManager


class Dividend(BaseModel):
    date: str
    label: str
    adjDividend: float
    dividend: float
    recordDate: str
    paymentDate: str
    declarationDate: str
    

class FmpDividens(FMPQueryManager):
    
    def historical(self, ticker:str) -> List[Dividend]:
        """
        https://site.financialmodelingprep.com/developer/docs#dividends-historical-dividends
        
        Dividends historical
        -
        Devuelve una lista con los dividendos pagados de la empresa a los socios
        
        Params
        -
         :param ticker (str)

        Returns
        -
            list of dictionaries

        
        """
        response = self.get(f'/api/v3/historical-price-full/stock_dividend/{ticker}')

        # Extraer la lista de dividendos del campo "historical" y diferenciarlo de "symbol"
        historical_data = response.get("historical", [])

        # Validar y devolver los dividendos como una lista de objetos Dividend
        return [Dividend.model_validate(r) for r in historical_data]