from investbook.sources.fmp.base import FMPQueryManager

class FmpFinancialStates(FMPQueryManager):
    
    def financial_states(self, ticker: str, period: str):
        """
        https://site.financialmodelingprep.com/developer/docs#income-statements-financial-statements    
     
        Income statement 
        -
        Devuelve una lista con el acceso en tiempo real a los datos de la cuenta de resultados de una amplia gama de empresas
        
        Params
        -
         :param ticker (str)
         :param period (str): annual | quarter

        Returns
        -
            list of dictionaries

        """
        return self.get(f'/v3/income-statement/{ticker}', period=period)
    