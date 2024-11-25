from investbook.sources.fmp.endpoints import FmpTickers

class FMPAPI:

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    @property
    def info(self):
         return FmpTickers(self._api_key)