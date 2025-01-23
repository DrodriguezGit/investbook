from .info import YahooFinanceInfo
from .historical import YahooFinanceHistorical

class YfinanceAPI:

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    @property
    def info(self):
        return YahooFinanceInfo()

    @property
    def stocks(self):
        return YahooFinanceHistorical()
