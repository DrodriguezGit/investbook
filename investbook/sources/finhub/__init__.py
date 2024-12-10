from investbook.sources.finhub.endpoints.info import FinHubInfo
from investbook.sources.finhub.endpoints.quote import FinHubQuote


class FINHUBAPI:

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    @property
    def get_symbol(self):
        return FinHubInfo(self._api_key)
    
    @property
    def get_quote(self):
        return FinHubQuote(self._api_key)
     
