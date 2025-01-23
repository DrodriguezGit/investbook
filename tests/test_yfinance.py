from investbook.sources.yfinance.info import YahooFinanceInfo
from investbook.sources.yfinance.historical import YahooFinanceHistorical
from pprint import pprint


yahoo_info = YahooFinanceInfo()

yahoo_historical = YahooFinanceHistorical()


# Consultar la información básica para el ticker 'AAPL' (Apple)
aapl_info = yahoo_info.get_info("AAPL")

# Imprimir la información obtenida
print(aapl_info)

googl_info = yahoo_info.get_info("GOOGL")

print(googl_info)


hist_appl = yahoo_historical.get_historical_data("AAPL", period="1y")  
pprint(hist_appl[0])  

# Obtener datos históricos
historical_data = yahoo_historical.get_historical_data("AAPL", period="1y")
for record in historical_data[:5]:  # Muestra los primeros 5 registros históricos
    print(record)