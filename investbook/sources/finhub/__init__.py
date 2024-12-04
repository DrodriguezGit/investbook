from investbook.sources.finhub.endpoints.test import FinHubSymbolLookup

class FINHUBAPI:

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    @property
    def get_symbol(self):
        return FinHubSymbolLookup(self._api_key)
     
