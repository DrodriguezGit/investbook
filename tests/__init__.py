from investbook.sources import AssetsAPI

API_KEY='1DWuCVNmdWPBcfL8R9pffQ9UacVGA9lK'

api = AssetsAPI(API_KEY)

api.polygon.stocks.get_price()
