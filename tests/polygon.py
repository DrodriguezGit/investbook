API_KEY='1DWuCVNmdWPBcfL8R9pffQ9UacVGA9lK'

from investbook.sources.polygon import PolygonAPI

api = PolygonAPI(api_key=API_KEY)

r = api.get_tickers()

from pprint import pprint
pprint(r)


#####

from investbook.sources import DataSources


sources = DataSources()


sources.polygon.get_tickers()

sources.alphavantage