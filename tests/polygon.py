from investbook.sources.polygon import PolygonAPI
from pprint import pprint

API_KEY='1DWuCVNmdWPBcfL8R9pffQ9UacVGA9lK'
polygon = PolygonAPI(api_key=API_KEY)

t = polygon.info.get_tickers(ticker='AAPL') 
pprint(t[0].name)

s = polygon.stocks.get_price('TSLA', '2024-11-18')
# Stocks prices (ticker, date)
pprint(s.date)
#Revisa

i = polygon.indices.get_price('I:AGQIV', '2023-03-10')
# Indices prices (I:ticker, date)
pprint(i.close)
exit()

c = polygon.cryptos.get_price('BTC', 'EUR', '2024-11-04')
# Crypto prices (crypto, currency, date)
pprint(c.close)
