from investbook.sources.fmp import FMPAPI
from pprint import pprint

#4Y2glVed0qPOPExJM2Hrj2f4mUPUSPPP
#UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4
API_KEY='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4'
fmp = FMPAPI(api_key=API_KEY)

info = fmp.stock.fundamentals("TSLA")
print(info.current_price)



historical = fmp.historical.historical("TSLA")
pprint(historical[-1])
#porque es una lista de 3 resultados

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


