
#%%
from investbook.sources.polygon import PolygonAPI
from pprint import pprint

API_KEY='1DWuCVNmdWPBcfL8R9pffQ9UacVGA9lK'
polygon = PolygonAPI(api_key=API_KEY)

#%%
t = polygon.info.get_tickers(market='', type='', search='tesla') 
# Markets = stocks, crypto, fx, otc, indices   / search: Si no sabes el nombre de la empresa, busca coincidencias
# pprint(t)
print(f"Count: {t['count']}")
for r in t['results']:
    print(f"Name: {r['name']}, Ticker: {r['ticker']}, Market: {r['market']}")


s = polygon.stocks.get_price('TSLA', '2024-11-18')
# Stocks prices (ticker, date)
pprint(f"Close: {s['close']}, High: {s['high']}")



i = polygon.indices.get_price('I:AGQIV', '2023-03-10')
# Indices prices (I:ticker, date)
pprint(i)


c = polygon.cryptos.get_price('BTC', 'EUR', '2024-11-04')
# Crypto prices (crypto, currency, date)
pprint(f"Precio de apertura: {c['open']},Precio de cierre: {c['close']}")

# %%
