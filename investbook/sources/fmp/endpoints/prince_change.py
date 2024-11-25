from investbook.sources.fmp.base import FMPQueryManager

class FmpPriceChange(FMPQueryManager):
    
    def price_change(self, ticker: str):
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
        return self.get(f'/v3/stock-price-change/{ticker}')