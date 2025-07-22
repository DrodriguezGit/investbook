from investbook.sources.finhub import FINHUBAPI
from pprint import pprint

#Si da: "Error: Too Many Requests. Rate limited. Try after a while." cambiar api_key en su web
API_KEY='d1v22gpr01qujmdf7890d1v22gpr01qujmdf789g'
finhub = FINHUBAPI(api_key=API_KEY)

# s = finhub.get_symbol.get_symbol('TSLA') 
# pprint(s)

s = finhub.get_symbol.get_status('US')
pprint(s.isOpen)

# t = finhub.get_symbol.get_trends('AAPL')
# pprint(t)

# q = finhub.get_quote.get_cuote('IDEXY')
# pprint(q.c)

# p = finhub.get_symbol.company_profile('IDEXY')
# pprint(p)

# news = finhub.get_symbol.company_news('TSLA')
# for article in news:
#     print(f"Headline: {article.headline}")
#     print(f"Summary: {article.summary}")
#     print(f"URL: {article.url}")

