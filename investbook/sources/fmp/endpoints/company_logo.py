from investbook.sources.fmp.base import FMPQueryManager

class FmpCompanyLogo(FMPQueryManager):
    
    def company_logo(self, logo: str):
        
        """
        https://site.financialmodelingprep.com/developer/docs#company-logo
        
        
        Company logo
        -
        Devuelve un .png con el logo 
        
        Params
        -
         :param logo (str)

        Returns
        -
            list of dictionaries

        """
        return self.get(f'image-stock/{logo}')
    
    #Endpoint de pago
    # def stock_peers(self, symbol: str):
    #     return self.get('v4/stock_peers', symbol=symbol)
