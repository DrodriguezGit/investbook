from __future__ import annotations
from nicegui import ui, Client
from investbook.sources.yfinance.historical import YahooFinanceHistorical
from investbook.sources import AssetsAPI
from investbook.app.front.shared.layout import Layout
from investbook.app.front.shared.colors import Colors
from datetime import datetime, timedelta
from investbook.sources.yfinance.info import YahooFinanceInfo  
from datetime import datetime, timedelta

class Cache:
    def __init__(self, cache_expiry: timedelta = timedelta(hours=3)):
        self.cache_expiry = cache_expiry
        self.cache_data = {}

    def load_cache(self, ticker: str):
        if ticker in self.cache_data:
            cache_entry = self.cache_data[ticker]
            cache_time = cache_entry['timestamp']
            if datetime.now() - cache_time < self.cache_expiry:
                return cache_entry['data']
        return None

    def save_cache(self, ticker: str, data):
        cache_entry = {
            'timestamp': datetime.now(),
            'data': data
        }
        self.cache_data[ticker] = cache_entry

    def get(self, ticker: str):
        return self.load_cache(ticker)

    def set(self, ticker: str, data):
        self.save_cache(ticker, data)




class Main:
    def __init__(self) -> None:
        tickers = ['AMZN', 'GOOGL', 'META', 'TSLA', 'NVDA', 'NFLX']
        self.cache = Cache()
        self.charts = {}  # Diccionario para almacenar instancias de gráficos por ticker

        @ui.page('/')
        def create_stock_cards(client: Client):
            client.layout.classes(Colors.body)

            with ui.row():
                search_input = ui.input()

                ui.button('Buscar', on_click=lambda: self.create_stock_card(client, search_input.value)).classes('bg-blue-500 text-white px-4 py-2 rounded-lg shadow-lg hover:bg-blue-400')

            with ui.row().classes('grid grid-cols-2 gap-20 mx-auto w-full justify-evenly').style('padding-left: 30px; padding-right: 30px;'):
                for i in range(2):
                    with ui.column().classes('w-full'):
                        with ui.row().classes('w-full'):
                            self.create_stock_card(client, tickers[i])
                        # with ui.row().classes('w-full mt-4'):  
                        #     self.create_stock_card(client, tickers[i+2])
                            
                        

    def e_chart(self, ticker: str, period: str, historical_data: list):
        """Genera o actualiza un gráfico de precios históricos."""
        if historical_data:
            #Seleccionamos la cantidad de días que corresponden
            days = {
                "1 Semana": 7,
                "1 Mes": 30,
                "3 Meses": 90,
                "6 Meses": 180,
                "1 Año": 365
            }.get(period, 365)

            #Nos quedamos con la selección de días
            filtered_data = historical_data[-days:]
            
            #Sacamos fecha y precio de datos filtrados
            dates = [data.date for data in filtered_data]
            close_prices = [data.close for data in filtered_data]

            return ui.echart({
                'xAxis': {
                    'type': 'category',
                    'data': dates,
                    'axisLabel': {'fontSize': 10}
                },
                'yAxis': {
                    'type': 'value'
                },
                'series': [{
                    'data': [f"{price:.2f}" for price in close_prices],
                    'type': 'line',
                    'smooth': True,
                    'areaStyle': {'color': 'rgba(0, 112, 243, 0.2)'},
                    'lineStyle': {'color': '#0070F3', 'width': 3}
                }],
                'tooltip': {
                    'trigger': 'axis'
                }
            }).classes('w-full h-60 rounded-lg shadow-lg mt-8').style('width: 100%; height: 400px;')

    def apply_filter(self, ticker: str, period: str, historical_data: list):
        """Actualiza el gráfico de la tarjeta correspondiente."""
        chart = self.charts.get(ticker)
        if chart:
            # Eliminar el gráfico actual
            chart.delete()

        
        days = {
            "1 Semana": 7,
            "1 Mes": 30,
            "3 Meses": 90,
            "6 Meses": 180,
            "1 Año": 365
        }.get(period, 365)

        filtered_data = historical_data[-days:]
        
        # Generar el nuevo gráfico llamando a la función de nuevo
        new_chart_options = self.e_chart(ticker, period, filtered_data)

        #Guarda el nuevo gráfico en el diccionario self.charts con el ticker como clave
        self.charts[ticker] = new_chart_options


    def fetch_data_from_api(self, ticker: str):
        yahoo_historical = YahooFinanceHistorical()
        historical_data = yahoo_historical.get_historical_data(ticker, period="1y")
        return historical_data


    def get_stock_data(self, ticker: str):
        cached_data = self.cache.get(ticker)

        if cached_data:
            print(f"Usando datos de caché para {ticker}")
            return cached_data
        else:
            data = self.fetch_data_from_api(ticker)
            self.cache.set(ticker, data)
            return data


    def create_stock_card(self, client: Client, ticker: str, period: str = "1y"):
        try:
            historical_data = self.get_stock_data(ticker)
            yahoo_info = YahooFinanceInfo()
            info_ticker = yahoo_info.get_info(ticker)
            company_name = info_ticker.company_name if info_ticker else "N/A"
            
            dates = [data.date for data in historical_data] if historical_data else []
            close_prices = [data.close for data in historical_data] if historical_data else []
            

        except Exception as e:
            print(f"Error: {e}")
            return

        with ui.card().classes('w-full p-6 rounded-xl shadow-lg bg-blue-50') as card:
            with ui.row().classes('flex gap-7'):
                with ui.column().classes('flex-1'):
                    ui.label(company_name).classes('text-3xl text-gray-800 text-left font-semibold')    
                    ui.label(f'({ticker})').classes('text-sm font-medium text-gray-500')
                    if historical_data:
                        ui.label(f'${historical_data[-1].close:,.2f}').classes('text-4xl text-right font-extrabold text-gray-800')
                    else:
                        ui.label(f'No disponible').classes('text-4xl text-right font-extrabold text-gray-800')

                    ui.button('Ver más datos', on_click=lambda:  ui.navigate.to(f"/info/{ticker}"))
                    
                    
                with ui.column().classes('flex-none w-52 h-aut  ml-40'):
                    if historical_data:
                        formatted_close_prices = [f"{price:.2f}" for price in close_prices]
                        chart = ui.echart({
                            'xAxis': {
                                'type': 'category',
                                'data': dates,
                                'axisLabel': {'fontSize': 10}
                            },
                            'yAxis': {
                                'type': 'value'
                            },
                            'series': [{
                                'data': formatted_close_prices,
                                'type': 'line',
                                'smooth': True,
                                'areaStyle': {'color': 'rgba(0, 112, 243, 0.2)'},
                                'lineStyle': {'color': '#0070F3', 'width': 3}
                            }],
                            'tooltip': {
                                'trigger': 'axis'
                            }
                        }).classes('w-80 h-60 rounded-lg shadow-sm justify-center items-center ')

                    else:
                        ui.label("No disponible").classes(' text-center text-gray-500')


            ui.button('X', on_click=lambda: card.delete()).classes('absolute top-2 right-2 p-2 bg-black text-white font-bold hover:bg-gray-800 transition-all duration-200').style(
                'width: 25px; height: 20px; border-radius: 10px;')


            with ui.row().classes('w-full mt-6 '):
                with ui.column().classes('w-full'):
                    with ui.tabs().classes('mb-0 w-full justify-center items-center').style('border-bottom: 2px solid #e2e8f0') as tabs:
                        pl = ui.tab('Información básica')
                        bl = ui.tab('Precio')
                        cf = ui.tab('Datos Financieros')

                    with ui.tab_panels(tabs, value=bl).classes('w-full'):
                        with ui.tab_panel(pl).classes('bg-blue-50'):
                            ui.label(f"Nombre: {info_ticker.company_name}").classes('text-base text-gray-700')
                            ui.label(f"Símbolo: {info_ticker.symbol}").classes('text-base text-gray-700')
                            ui.label(f"Sector: {info_ticker.sector}").classes('text-base text-gray-700')
                            ui.label(f"Industria: {info_ticker.industry}").classes('text-base text-gray-700')
                            ui.label(f"País: {info_ticker.country}").classes('text-base text-gray-700')
                        
                        with ui.tab_panel(bl).classes('bg-blue-50 p-6 rounded-lg shadow-lg w-full'):
                            with ui.column().classes('w-full gap-4 items-center'):
                                with ui.row().classes('w-full justify-center gap-4'):
                                    for period in ["1 Semana", "1 Mes", "3 Meses", "6 Meses", "1 Año"]:
                                        ui.button(period, on_click=lambda p=period: self.apply_filter(ticker, p, historical_data)) \
                                            .classes('bg-white text-black font-semibold px-6 py-3 rounded-lg shadow-md hover:bg-gray-200')

                                # Contenedor para el gráfico (ocupa todo el ancho)
                                with ui.row().classes('w-full justify-center'):
                                    chart = self.charts.get(ticker)
                                    if chart:
                                        chart.delete()
                                        self.e_chart(ticker, "1 Semana", historical_data)

                                

                        with ui.tab_panel(cf).classes('bg-blue-50 p-4 rounded-lg shadow-lg'):
                                with ui.column().classes('gap-2 p-4 rounded-lg shadow-sm w-80'):
                                    ui.label(f"Capitalización de mercado: ${info_ticker.market_cap:,.2f}").classes('text-base text-gray-700')
                                    ui.label(f"Precio actual: ${historical_data[-1].close:,.2f}").classes('text-base text-gray-700')
                                    ui.label(f"Cierre anterior: ${historical_data[-2].close:,.2f}").classes('text-base text-gray-700')
                                    ui.label(f"Dividendos: {info_ticker.dividend_yield}%").classes('text-base text-gray-700')
                                    ui.label(f"Ingresos totales: ${info_ticker.total_revenue:,.2f}").classes('text-base text-gray-700')
