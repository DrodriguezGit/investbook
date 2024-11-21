from .endpoints import (
    PolygonEndpointStocks,
    PolygonEndpointCrypto,
    PolygonEndpointIndex,
    PolygonEndpointInfo,
    PolygonEndpointOption
)

class PolygonAPI:

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    @property
    def info(self):
        return PolygonEndpointInfo(self._api_key)

    @property
    def stocks(self):
        return PolygonEndpointStocks(self._api_key)

    @property
    def options(self):
        return PolygonEndpointOption(self._api_key)

    @property
    def indices(self):
        return PolygonEndpointIndex(self._api_key)

    @property
    def cryptos(self):
        return PolygonEndpointCrypto(self._api_key)
    