from ..base import PolygonQueryManager


class PolygonEndpointOption(PolygonQueryManager):

    def get_option_contract(self, ticker: str) -> dict:
        '''
        ¿STRIKES?
        '''
        return self.get(f'v3/reference/options/contracts/{ticker}')
    
    def get_price(self, option_ticker: str, date: str) -> dict:
        '''
        https://polygon.io/docs/options/get_v1_open-close__optionsticker___date
        '''
        return self.get(f'/v1/open-close/{option_ticker}/{date}')