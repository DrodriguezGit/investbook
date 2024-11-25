from investbook.sources.fmp import FMPAPI
from pprint import pprint

API_KEY='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4'
fmp = FMPAPI(api_key=API_KEY)

s = fmp.info.stock_list() 
pprint(s[:2])

p = fmp.info.company_profile('AAPL')
pprint(p)

c = fmp.info.company_logo('EURUSD.png')
#
pprint(c)

q = fmp.info.quote('AAPL')
pprint(q)

pc = fmp.info.price_change('AAPL')
pprint(pc)

fs = fmp.financial_states('AAPL', 'annual')
pprint(fs)

dh = fmp.info.dividends_historical('AAPL')
pprint(dh)

