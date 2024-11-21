from investbook.sources.polygon import PolygonAPI
from pprint import pprint

API_KEY='1DWuCVNmdWPBcfL8R9pffQ9UacVGA9lK'
api = PolygonAPI(api_key=API_KEY)

t = api.get_tickers(market='', type='', search='tesla') 
# Markets = stocks, crypto, fx, otc, indices   / search: Si no sabes el nombre de la empresa, busca coincidencias
# pprint(t)
print(f"Count: {t['count']}")
for r in t['results']:
    print(f"Name: {r['name']}, Ticker: {r['ticker']}, Market: {r['market']}")


s = api.get_price_stock('TSLA', '2024-11-18')
# Stocks prices (ticker, date)
pprint(f"Close: {s['close']}, High: {s['high']}")


oc = api.get_option_contract('TSLZ')
pprint(oc)
o = api.get_price_option('TSLZ', '2024-11-12')
# Option prices (ticketr, date)#################### Ahondar en los contratos de opciones
pprint(o)


i = api.get_price_indice('I:AGQIV', '2023-03-10')
# Indices prices (I:ticker, date)
pprint(i)


c = api.get_price_crypto('BTC', 'EUR', '2024-11-04')
# Crypto prices (crypto, currency, date)
pprint(f"Precio de apertura: {c['open']},Precio de cierre: {c['close']}")
