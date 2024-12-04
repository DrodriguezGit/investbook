from investbook.sources.finhub.base import FinHubQueryManager

class FinHubSymbolLookup(FinHubQueryManager):
        
    def get_symbol(self, q: str):
        """
        https://finnhub.io/docs/api/symbol-search
        """
        return self.get(f'/search?{q}')

    
    