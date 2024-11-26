from investbook.sources.fmp.endpoints import (
    FmpStockList,
    FmpCompanyProfile,
    FmpCompanyLogo,
    FmpQuote,
    FmpPriceChange,
    FmpFinancialStates,
    FmpDividensHistorical 
)

class FMPAPI:

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    @property
    def stock_list(self):
        return FmpStockList(self._api_key)
     
    @property
    def profile(self):
        return FmpCompanyProfile(self._api_key)
    
    @property
    def logo(self):
        return FmpCompanyLogo(self._api_key)
     
    @property
    def quote(self):
        return FmpQuote(self._api_key)
     
    @property
    def price(self):
        return FmpPriceChange(self._api_key)
     
    @property
    def finance(self):
        return FmpFinancialStates(self._api_key)
     
    @property
    def dividends(self):
        return FmpDividensHistorical(self._api_key)