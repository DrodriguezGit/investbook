from nicegui import ui, Client
from investbook.sources import AssetsAPI  
from investbook.app.front.shared.layout import Layout
from investbook.app.front.shared.colors import Colors



class Prices:
    
    def __init__(self) -> None:

        @ui.page('/fmp/price/{ticker}') 
        async def root(client: Client, ticker: str):

            client.layout.classes(Colors.body)
            Layout()

            try:
                api = AssetsAPI(fmp_api_key='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4')
                price_data = api.fmp.price.change(ticker)  
                
                
            except Exception as e:
                print(e)
                
            if price_data:
                
                price = price_data[0]
                ui.label(f"Símbolo: {price.symbol}")
                ui.label(f"Variación diaria: {price.day}")
                ui.label(f"Variación semanal: {price.week}")
                ui.label(f"Variación mensual: {price.month}")
                ui.label(f"Variación anual: {price.year}")
                ui.label(f"Año hasta la fecha: {price.ytd}")
                ui.label(f"Máximo: {price.max}")
            else:
                ui.label(f"No se encontraron datos para el ticker {ticker}")
                
                
     