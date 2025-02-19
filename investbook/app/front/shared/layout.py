from investbook.app.front.components.layout.header import Header
from investbook.app.front.components.layout.menu import NavigationMenu, NavItem

class Layout:

    def __init__(self) -> None:
        self.left_drawer = None(
            items=[
            NavItem(text='Inicio', rt='/', icon='home'),
            NavItem(text='Information', rt='/yfinance/info', icon='info'),
            NavItem(text='Historical Data', rt='/yfinance/historical', icon='bar_chart')
        ]
            # items=[
            #     NavItem(text='Inicio', rt='/', icon='home'),
            #     NavItem(
            #         text='Proveedores de datos',
            #         subitems=[
            #             NavItem(
            #                 text='Polygon.io',
            #                 subitems=[
            #                     NavItem(text='Cryptos', rt='/polygon/cryptos', icon='currency_bitcoin'),
            #                     NavItem(text='Indices', rt='/polygon/indices', icon='bar_chart'),
            #                     NavItem(text='Stocks', rt='/polygon/stocks', icon='trending_up')
            #                 ],
            #             ),
            #             NavItem(
            #                 text='FMP',
            #                 subitems=[
            #                     NavItem(text='Company', rt='/fmp/company', icon='business'),
            #                     NavItem(text='Dividends', rt='/fmp/dividends', icon='attach_money'),
            #                     NavItem(text='Financials', rt='/fmp/financials', icon='account_balance'),
            #                     NavItem(text='Price', rt='/fmp/price', icon='price_check')
            #                 ],
            #             ),
            #             NavItem(
            #                 text='Finhub',
            #                 subitems=[
            #                     NavItem(text='Info Stocks', rt='/finhub/info', icon='info')
            #                 ],
            #             ),
                        
            #             NavItem(
            #                 text='Yahoo Finance',
            #                 subitems=[
            #                     NavItem(text='Info Stocks', rt='/yfinance/info', icon='info'),
            #                     NavItem(text='Historical Data', rt='/yfinance/historical', icon='info')
            #                 ],
            #             ),
            #         ]
            #     ),
            # ]
        )

        self.header = Header(left_drawer=self.left_drawer)