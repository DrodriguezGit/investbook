from investbook.sources.fmp import FMPAPI
from pprint import pprint

API_KEY='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4'
fmp = FMPAPI(api_key=API_KEY)

sl = fmp.stock.list()
pprint(sl[0].name)

s = fmp.stock.info('AAPL')
pprint(s[0].price)


p = fmp.company.get_profile('AAPL') 
pprint(p[0].city)


c = fmp.company.get_logo('EURUSD.png')  
c.save('EURUSD.png')

pc = fmp.price.change('AAPL')
pprint(pc.day)

fs = fmp.finance.income_statement('LYG', 'annual')
pprint(fs[0].netIncomeRatio)

dh = fmp.dividends.historical('LYG')
pprint(dh[0].date)




