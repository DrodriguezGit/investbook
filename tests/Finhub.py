from investbook.sources.finhub import FINHUBAPI
from pprint import pprint

API_KEY='culmc89r01qovv70aj10culmc89r01qovv70aj1g'
finhub = FINHUBAPI(api_key=API_KEY)

# s = finhub.get_symbol.get_symbol('apple') 
# pprint(s)

# # s = finhub.get_symbol.get_status('US')
# # pprint(s)

# t = finhub.get_symbol.get_trends('AAPL')
# pprint(t)

# q = finhub.get_quote.get_cuote('IDEXY')
# pprint(q)

# p = finhub.get_symbol.company_profile('IDEXY')
# pprint(p)

news = finhub.get_symbol.company_news('TSLA')
for article in news:
    print(f"Headline: {article.headline}")
    print(f"Summary: {article.summary}")
    print(f"URL: {article.url}")

