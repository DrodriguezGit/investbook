from investbook.sources.fmp.base import FMPQueryManager

class FmpStockList(FMPQueryManager):
        
    def stock_list(self):
        """
        https://site.financialmodelingprep.com/developer/docs#symbol-list-stock-list

        Ticker stock companies
        -
        Devuelve una lista de los tickers, el exchange y el nombre de las empresas


        Returns
        -
            list of dictionaries
        """
        return self.get(f'/v3/stock/list')

    
    
