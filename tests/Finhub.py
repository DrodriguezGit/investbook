from investbook.sources.finhub import FINHUBAPI
from pprint import pprint

API_KEY='ct8pt19r01qpc9s002l0ct8pt19r01qpc9s002lg'
finhub = FINHUBAPI(api_key=API_KEY)

s = finhub.get_symbol.get_symbol('apple') 
pprint(s)

# s = finhub.get_symbol.get_status('US')
# pprint(s)

t = finhub.get_symbol.get_trends('AAPL')
pprint(t)

q = finhub.get_quote.get_cuote('IDEXY')
pprint(q)

p = finhub.get_symbol.company_profile('IDEXY')
pprint(p)

