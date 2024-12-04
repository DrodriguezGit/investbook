from investbook.sources.finhub import FINHUBAPI
from pprint import pprint

API_KEY='ct3igu1r01qrd05j401gct3igu1r01qrd05j4020'
finhub = FINHUBAPI(api_key=API_KEY)

s = finhub.get_symbol.get_symbol('apple') 
pprint(s)