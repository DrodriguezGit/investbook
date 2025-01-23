from investbook.sources.polygon import PolygonAPI
from pprint import pprint

API_KEY='1DWuCVNmdWPBcfL8R9pffQ9UacVGA9lK'
polygon = PolygonAPI(api_key=API_KEY)

t = polygon.info.get_tickers(ticker='AAPL') 
pprint(t)

s = polygon.stocks.get_price('TSLA', '2024-12-23') 
# Stocks prices (ticker, date)
pprint(s)

i = polygon.indices.get_price('I:AGQIV', '2023-03-10')
# Indices prices (I:ticker, date)
pprint(i)

c = polygon.cryptos.get_price('BTC', 'EUR', '2024-11-04')
# Crypto prices (crypto, currency, date)
pprint(c.close)
