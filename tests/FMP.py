from investbook.sources.fmp import FMPAPI
from pprint import pprint

API_KEY='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4'
fmp = FMPAPI(api_key=API_KEY)

s = fmp.stock_list.stock_list() 
pprint(s[:2])

p = fmp.profile.company_profile('LYG') #Probado con 'LYG' y 'AAPL'
pprint(p)

c = fmp.logo.company_logo('EURUSD.png', save_path='EURUSD_logo.png')  #Guarda el png en el directorio de investbook
pprint(c)

q = fmp.quote.quote('LYG')
pprint(q)

pc = fmp.price.price_change('LYG')
pprint(pc)

fs = fmp.finance.financial_states('LYG', 'annual')
pprint(fs)

dh = fmp.dividends.dividends_historical('LYG')
pprint(dh)

