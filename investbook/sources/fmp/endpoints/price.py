from pydantic import BaseModel, Field
from typing import Optional, List

from investbook.sources.fmp.base import FMPQueryManager

class Price(BaseModel):
    symbol: Optional[str]
    day: Optional[float] = Field(None, alias='1D')
    week: Optional[float] = Field(None, alias='5D')
    month: Optional[float] = Field(None, alias='1M')
    year: Optional[float] = Field(None, alias='1Y')
    ytd: Optional[float]
    max: Optional[float]


class FmpPrice(FMPQueryManager):
    
    def change(self, ticker: str) -> List[Price]:
        """
        https://site.financialmodelingprep.com/developer/docs#stock-price-change-quote

        Stock prices 
        -
        Devuelve una lista con el precio del activo en diferentes rangos de tiempo
        
        Params
        -
         :param ticker (str)

        Returns
        -
            list of dictionaries

        """
        return [Price.model_validate(r) for r in self.get(f'/api/v3/stock-price-change/{ticker}')][0]
    
    
    