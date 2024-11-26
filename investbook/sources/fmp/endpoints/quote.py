from investbook.sources.fmp.base import FMPQueryManager

class FmpQuote(FMPQueryManager):
    
    def quote(self, ticker: str): 
        """
        https://site.financialmodelingprep.com/developer/docs#full-quote-quote

        Company names 
        -
        Devuelve una lista con empresas que están en el mismo exchange, sector o capitalización de mercado similar
        
        Params
        -
         :param ticker (str)

        Returns
        -
            list of dictionaries

        """
        return self.get(f'/api/v3/quote/{ticker}')
    