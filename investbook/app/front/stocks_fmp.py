from __future__ import annotations

from nicegui import ui, Client

from investbook.sources import AssetsAPI

from investbook.app.front.shared.layout import Layout

from investbook.app.front.shared.colors import Colors



class Stocks_fmp:
    
    def __init__(self) -> None:

        @ui.page('/stocks/{ticker}')
        async def root(client: Client, ticker: str):

            client.layout.classes(Colors.body)
            Layout()

            stock_info = None

            try:
                api = AssetsAPI(fmp_api_key='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4')

                stock_list = api.fmp.stock.list()  
                stock_info = api.fmp.stock.info(ticker)  

            except Exception as e:
                print(e)

            # Encontramos la acción seleccionada en la lista de 'list'
            selected_stock = next((stock for stock in stock_list if stock.symbol == ticker), None)

            if selected_stock:
                
                ui.label(f"Información básica de la acción: {selected_stock.name} ({selected_stock.symbol})").style('font-weight: bold')
                ui.label(f"Exchange: {selected_stock.exchangeShortName}")
                ui.label(f"Precio: ${selected_stock.price}")
            
            
            if stock_info:

                info = stock_info[0]
                ui.label(f"  ")
                ui.label(f"Información avanzada de la acción").style('font-weight: bold')
                ui.label(f"Precio de apertura del día: ${info.dayLow} - ${info.dayHigh}")
                ui.label(f"Capitalización de mercado: ${info.marketCap:,}")
                ui.label(f"Volumen: {info.volume}")
                ui.label(f"Cambio porcentual: {info.changesPercentage}%")
                ui.label(f"Precio promedio 50 días: ${info.priceAvg50}")
                ui.label(f"Precio promedio 200 días: ${info.priceAvg200}")

            else:
                ui.label(f"No se encontraron detalles para la acción {ticker}")
  