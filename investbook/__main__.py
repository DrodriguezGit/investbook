from investbook.app.front.index import Main
from investbook.app.front.stocks_fmp import Stocks_fmp
from investbook.app.front.indices import Indices
from investbook.app.front.price import Prices
from investbook.app.front.financials import Financials
from investbook.app.front.dividends import Dividends
from investbook.app.front.company import Company
from investbook.app.front.info_finhub import Info_finhub
from investbook.app.front.info import Info
from investbook.app.front.stocks_polygon import Stocks_pol
from investbook.app.front.crypto import Crypto
from investbook.app.front.Info_yahoo import Info_yahoo
from investbook.app.front.historical import HistoricalData
from nicegui import ui


Main()
Stocks_fmp()
Indices()
Prices()
Financials()
Dividends()
Company()
Info_finhub()
Stocks_pol()
Crypto()
Info_yahoo()
HistoricalData()
Info()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run()