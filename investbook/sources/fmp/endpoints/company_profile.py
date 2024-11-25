from investbook.sources.fmp.base import FMPQueryManager

class FmpCompanyProfile(FMPQueryManager):
       
    def company_profile(self, ticker: str):
        """
        https://site.financialmodelingprep.com/developer/docs#company-profile-company-information


        Profile companies
        -
        Devuelve una lista con toda la información básica del ticker 
        
        Params
        -
         :param ticker (str)

        Returns
        -
            list of dictionaries
        """
        return self.get(f'/v3/profile/{ticker}')
    