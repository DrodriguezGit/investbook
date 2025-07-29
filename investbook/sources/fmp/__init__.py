from investbook.sources.fmp.endpoints import (
    FmpStock,
    FmpCompany,
    FmpPrice,
    FmpFinancialStates,
    FmpDividens,
    FmpHistorical
)

class FMPAPI:

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    @property
    def stock(self):
        return FmpStock(self._api_key)
    
    @property
    def historical(self):
        return FmpHistorical(self._api_key)
     
    @property
    def company(self):
        return FmpCompany(self._api_key)

    @property
    def price(self):
        return FmpPrice(self._api_key)
     
    @property
    def finance(self):
        return FmpFinancialStates(self._api_key)
     
    @property
    def dividends(self):
        return FmpDividens(self._api_key)