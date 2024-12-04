from investbook.sources.fmp import FMPAPI
from pprint import pprint

API_KEY='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4'
fmp = FMPAPI(api_key=API_KEY)

sl = fmp.stock.list()
pprint(sl.exchange)
#Con los corchetes da un TypeError:'Stock' object is not subscriptable pero se pueden llamar a los objetos igual
#Sin los corchetes no da error, no aparecen los objetos a llamar en pprint, pero funcionan igual

s = fmp.stock.info('AAPL')
pprint(s.price)
#Ocurre lo mismo que arriba, sin los corchetes no aparecen las opciones en el pprint pero puedes llamarlos igual

p = fmp.company.get_profile('AAPL')[0] #Este todo bien con los corchetes
pprint(p.price)

c = fmp.company.get_logo('EURUSD.png')  
c.save('EURUSD.png')

pc = fmp.price.change('AAPL')
pprint(pc.day)
#Pasa como en stock: sin corchetes no puedes llamar a los objetos pero funcionan

fs = fmp.finance.income_statement('LYG', 'annual')[0]
pprint(fs.costOfRevenue)
#Todo bien

dh = fmp.dividends.historical('LYG')[0]
pprint(dh.dividend)
#Todo bien


