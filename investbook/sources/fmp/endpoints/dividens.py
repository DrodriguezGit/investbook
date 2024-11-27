from investbook.sources.fmp.base import FMPQueryManager

class FmpDividens(FMPQueryManager):
    
    def historical(self, ticker:str):
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
        return self.get(f'/api/v3/historical-price-full/stock_dividend/{ticker}')
    