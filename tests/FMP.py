from investbook.sources.fmp import FMPAPI
from pprint import pprint

API_KEY='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4'
fmp = FMPAPI(api_key=API_KEY)


sl = fmp.stock.list()
pprint(sl)
pprint(sl[0])

exit()

s = fmp.stock.info('TSLA')
pprint(s)


p = fmp.company.get_profile('IDEXY') 
pprint(p)

# c = fmp.company.get_logo('EURUSD.png')  
# c.save('EURUSD.png')

pc = fmp.price.change('IDEXY')
pprint(pc)

fs = fmp.finance.income_statement('IDEXY', 'annual')
pprint(fs)

dh = fmp.dividends.historical('AAPL')
pprint(dh)

n = fmp.stock.news('AAPL')
pprint(n)


