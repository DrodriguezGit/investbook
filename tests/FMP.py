from investbook.sources.fmp import FMPAPI
from pprint import pprint

API_KEY='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4'
fmp = FMPAPI(api_key=API_KEY)

# s = fmp.stock.list()

# pprint(s[:2])

# p = fmp.company.get_profile('LYG') #Probado con 'LYG' y 'AAPL'
# pprint(p)

c = fmp.company.get_logo('EURUSD.png')  #Guarda el png en el directorio de investbook
c.save('EURUSD.png')

exit()

q = fmp.stock.info('LYG')
pprint(q)



pc = fmp.price.change('LYG')
pprint(pc)

fs = fmp.finance.income_statement('LYG', 'annual')
pprint(fs)

dh = fmp.dividends.historical('LYG')
pprint(dh)

