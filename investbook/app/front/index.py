# from __future__ import annotations
# from nicegui import ui, Client
# from investbook.sources.yfinance.historical import YahooFinanceHistorical
# from investbook.sources import AssetsAPI
# from investbook.app.front.shared.layout import Layout
# from investbook.app.front.shared.colors import Colors
# from datetime import datetime, timedelta
# from investbook.sources.yfinance.info import YahooFinanceInfo  
# from datetime import datetime, timedelta


# class Cache:
#     def __init__(self, cache_expiry: timedelta = timedelta(hours=3)):
#         self.cache_expiry = cache_expiry  # El tiempo que los datos son válidos
#         self.cache_data = {}  # Diccionario donde almacenaremos los datos

#     def load_cache(self, ticker: str):
#         """Obtiene los datos de la caché si no han expirado."""
#         if ticker in self.cache_data:
#             cache_entry = self.cache_data[ticker]
#             cache_time = cache_entry['timestamp']
#             # Verificar si la caché ha expirado
#             if datetime.now() - cache_time < self.cache_expiry:
#                 return cache_entry['data']
#         return None

#     def save_cache(self, ticker: str, data):
#         """Guarda los datos en la caché."""
#         cache_entry = {
#             'timestamp': datetime.now(),  # Guardamos la hora de la caché
#             'data': data
#         }
#         self.cache_data[ticker] = cache_entry

#     def get(self, ticker: str):
#         """Obtiene los datos del ticker desde la caché o None si no existen o están desactualizados."""
#         return self.load_cache(ticker)

#     def set(self, ticker: str, data):
#         """Establece los datos de la caché para un ticker específico."""
#         self.save_cache(ticker, data)



# class Main:
    
#     def __init__(self) -> None:
#         tickers = ['AMZN', 'GOOGL', 'META', 'TSLA', 'NVDA', 'NFLX']  
        
#         self.cache = Cache()  # Usamos la caché en memoria
        
#         @ui.page('/')
#         def create_stock_cards(client: Client):
#             client.layout.classes(Colors.body)
#             Layout()

                
#             with ui.row().classes('flex justify-evenly gap-4 mx-auto w-full px-4') as row: # Mx-auto Centra el contenedor horizontalmente en su espacio
#                 for i in range(3):  
#                     with ui.column().classes('w-full max-w-md p-4'):
#                         self.create_stock_card(client, tickers[i])

                
#             with ui.row().classes('flex justify-evenly gap-4 mx-auto w-full mt-8 px-4'): #justify-evenly distribuye los elementos de manera uniforme a lo largo del contenedor
#                 for i in range(3, 6):  
#                     with ui.column().classes('w-full max-w-md p-4'):
#                         self.create_stock_card(client, tickers[i])
        
#     def fetch_data_from_api(self, ticker: str):
#         """Simula la llamada a la API para obtener datos"""
#         yahoo_historical = YahooFinanceHistorical()
#         historical_data = yahoo_historical.get_historical_data(ticker, period="1y")


#     def get_stock_data(self, ticker: str):
#         """Obtiene los datos del stock, utilizando la caché si es posible"""
#         cached_data = self.cache.get(ticker)
        
#         if cached_data:
#             print(f"Usando datos de caché para {ticker}")
#             return cached_data
#         else:
#             # Si no hay datos en caché, obtener desde la API
#             data = self.fetch_data_from_api(ticker)
#             self.cache.set(ticker, data)  # Guardamos los datos en la caché
#             return data

                            
                            
#     def create_stock_card(self, client: Client, ticker: str, period: str = "1y"):
#         try:
            
#             yahoo_historical = YahooFinanceHistorical()
#             historical_data = yahoo_historical.get_historical_data(ticker, period)

            
#             api_fmp = AssetsAPI(fmp_api_key='4Y2glVed0qPOPExJM2Hrj2f4mUPUSPPP')
#             balance_data = api_fmp.fmp.finance.income_statement(ticker, period='annual')
            
#             if balance_data:
#                     balance = sorted(balance_data, key=lambda x: datetime.strptime(x.date, '%Y-%m-%d'), reverse=True)
#                     last_financial = balance[:1]

            
#             yahoo_info = YahooFinanceInfo()
#             info_ticker = yahoo_info.get_info(ticker)

#             company_name = info_ticker.company_name if info_ticker else "N/A"

            
#             dates = [data.date for data in historical_data] if historical_data else []
#             close_prices = [data.close for data in historical_data] if historical_data else []

#         except Exception as e:
#             print(f"Error: {e}")
#             return

        
#         with ui.card().classes('w-full p-6 rounded-xl shadow-lg bg-blue-50'):
#             with ui.column().classes('h-24'):
#                 ui.label(company_name).classes('text-3xl text-gray-800 text-right')

#                 for record in historical_data[0:1]:
#                     ui.label(f'${record.open:,.2f}').classes('text-4xl text-right font-extrabold text-gray-800')
                    
#                 ui.label(f'({ticker})').classes('text-sm font-medium text-gray-500').style('align-self: flex-start')

#             ui.separator().classes('my-8 border-gray-300')

            
#             with ui.column().classes('w-full') as container:
#                 with ui.tabs().classes('mb-4 w-full').style('border-bottom: 2px solid #e2e8f0 padding-left: 20px; padding-right: 20px') as tabs:
#                     pl = ui.tab('Bº')
#                     bl = ui.tab('BF')
#                     cf = ui.tab('RyMF')

#             with ui.tab_panels(tabs, value=pl):
#                 with ui.tab_panel(pl).classes('bg-blue-50'):
#                     with ui.column().classes('gap-2 p-4 rounded-lg shadow-sm w-80'):
#                         ui.label(f'Ingresos: ${info_ticker.total_revenue:,.2f}').classes('text-base text-gray-700')
#                         ui.label(f'Dividendos: ${info_ticker.dividend_yield:,.2f}').classes('text-base text-gray-700')
#                         ui.label(f'Ingreso Neto: ${info_ticker.net_income:,.0f}').classes('text-base text-gray-700')

#                 with ui.tab_panel(bl).classes('bg-blue-50'):
                    
#                     for financial in last_financial:
#                         with ui.column().classes('gap-2 p-4 rounded-lg shadow-sm w-80'):
#                             ui.label(f'Total Gastos: ${financial.costAndExpenses:,.0f}').classes('text-base text-gray-700')
#                             ui.label(f'Margen de beneficio neto: ${financial.netIncomeRatio * 100:,.2f}').classes('text-base text-gray-700')
#                             ui.label(f'EBITDA: ${financial.ebitda:,.0f}').classes('text-base text-gray-700')

#                 with ui.tab_panel(cf).classes('bg-blue-50'):
#                     with ui.column().classes('gap-2 p-4 rounded-lg shadow-sm w-80'):
#                         ui.label(f"Rent. sobre activos: {info_ticker.return_on_assets:,.2f}%").classes('text-base text-gray-700')
#                         ui.label(f"Deuda sobre capital: ${info_ticker.debt_to_equity:,.3f}").classes('text-base text-gray-700')
#                         ui.label(f"Ratio corriente: {info_ticker.current_ratio:,.3f}").classes('text-base text-gray-700')

            
            

            
#             if historical_data:
#                 formatted_close_prices = [f"{price:.2f}" for price in close_prices]
#                 linechart = ui.echart({
#                     'xAxis': {
#                         'type': 'category',
#                         'data': dates,  
#                         'axisLabel': {'fontSize': 10}
#                     },
#                     'yAxis': {
#                         'type': 'value'
#                     },
#                     'series': [{
#                         'data': formatted_close_prices,  
#                         'type': 'line',
#                         'smooth': True,
#                         'areaStyle': {'color': 'rgba(0, 112, 243, 0.2)'},
#                         'lineStyle': {'color': '#0070F3', 'width': 3}
#                     }],
#                     'tooltip': {
#                         'trigger': 'axis'
#                     }
#                 }).classes('w-full h-64 rounded-lg shadow-sm')


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
        self.cache_expiry = cache_expiry  # El tiempo que los datos son válidos
        self.cache_data = {}  # Diccionario donde almacenaremos los datos

    def load_cache(self, ticker: str):
        """Obtiene los datos de la caché si no han expirado."""
        if ticker in self.cache_data:
            cache_entry = self.cache_data[ticker]
            cache_time = cache_entry['timestamp']
            # Verificar si la caché ha expirado
            if datetime.now() - cache_time < self.cache_expiry:
                return cache_entry['data']
        return None

    def save_cache(self, ticker: str, data):
        """Guarda los datos en la caché."""
        cache_entry = {
            'timestamp': datetime.now(),  # Guardamos la hora de la caché
            'data': data
        }
        self.cache_data[ticker] = cache_entry

    def get(self, ticker: str):
        """Obtiene los datos del ticker desde la caché o None si no existen o están desactualizados."""
        return self.load_cache(ticker)

    def set(self, ticker: str, data):
        """Establece los datos de la caché para un ticker específico."""
        self.save_cache(ticker, data)




# class Main:
    
#     def __init__(self) -> None:
#         tickers = ['AMZN', 'GOOGL', 'META', 'TSLA', 'NVDA', 'NFLX']  
        
#         self.cache = Cache()  # Usamos la caché en memoria
#         @ui.page('/')
#         def create_stock_cards(client: Client):
        
#             client.layout.classes(Colors.body)
#             Layout()

#             with ui.row().classes('grid grid-cols-2 gap-4 mx-auto w-full px-2 justify-evenly'):
#                 for i in range(2):  # Primeras dos tarjetas
#                     with ui.column().classes('w-full'):  # Tarjeta ocupa toda la columna
#                         self.create_stock_card(client, tickers[i])

#             # with ui.row().classes('grid grid-cols-2 gap-4 mx-auto w-full px-2 justify-evenly'):
#             #     for i in range(2, 4):  # Primeras dos tarjetas
#             #         with ui.column().classes('w-full'):  # Tarjeta ocupa toda la columna
#             #             self.create_stock_card(client, tickers[i])
        

#     def fetch_data_from_api(self, ticker: str):
#         """Simula la llamada a la API para obtener datos"""
#         yahoo_historical = YahooFinanceHistorical()
#         historical_data = yahoo_historical.get_historical_data(ticker, period="1y")
#         return historical_data

#     def get_stock_data(self, ticker: str):
#         """Obtiene los datos del stock, utilizando la caché si es posible"""
#         cached_data = self.cache.get(ticker)
        
#         if cached_data:
#             print(f"Usando datos de caché para {ticker}")
#             return cached_data
#         else:
#             # Si no hay datos en caché, obtener desde la API
#             data = self.fetch_data_from_api(ticker)
#             self.cache.set(ticker, data)  # Guardamos los datos en la caché
#             return data

#     def create_stock_card(self, client: Client, ticker: str, period: str = "1y"):
#         try:
#             # Obtener los datos de la API (historical, balance, etc.)
#             historical_data = self.get_stock_data(ticker)
#             api_fmp = AssetsAPI(fmp_api_key='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4')
#             # balance_data = api_fmp.fmp.finance.income_statement(ticker, period='annual')
            
#             # if balance_data:
#             #     balance = sorted(balance_data, key=lambda x: datetime.strptime(x.date, '%Y-%m-%d'), reverse=True)
#             #     last_financial = balance[:1]

#             yahoo_info = YahooFinanceInfo()
#             info_ticker = yahoo_info.get_info(ticker)
#             company_name = info_ticker.company_name if info_ticker else "N/A"

#             dates = [data.date for data in historical_data] if historical_data else []
#             close_prices = [data.close for data in historical_data] if historical_data else []
            
#             api = AssetsAPI(fmp_api_key='4Y2glVed0qPOPExJM2Hrj2f4mUPUSPPP')
#             price_data = api.fmp.price.change(ticker)  

#         except Exception as e:
#             print(f"Error: {e}")
#             return

        
#         with ui.card().classes('w-2/3 rounded-xl shadow-lg bg-blue-50'):

#         # Primera fila con dos columnas (Cuadrante superior izquierdo y derecho)
#             with ui.row().classes('flex gap-7'):
                
#                 # Primer cuadrante: Información de la empresa (nombre, ticker, precio)
#                 with ui.column().classes('flex-1'):
#                     # Nombre de la empresa
#                     ui.label(company_name).classes('text-3xl text-gray-800 text-left font-semibold')
                    
#                     # Ticker de la empresa
#                     ui.label(f'({ticker})').classes('text-sm font-medium text-gray-500')
                    
#                     # Precio actual de la acción
#                     if historical_data:
#                         ui.label(f'${historical_data[0].close:,.2f}').classes('text-4xl text-right font-extrabold text-gray-800')
#                     else:
#                         ui.label(f'No disponible').classes('text-4xl text-right font-extrabold text-gray-800')

                    

#                 # Segundo cuadrante: Gráfico de precios (debe ir en la segunda columna) w-52 es el correcto
#                 with ui.column().classes('flex-none w-52 h-aut'):
#                     if historical_data:
#                         # Verificar que los precios y las fechas están disponibles
#                         if not dates or not close_prices:
#                             ui.label("Datos de gráfico no disponibles").classes('text-center text-gray-500')
#                         else:
#                             formatted_close_prices = [f"{price:.2f}" for price in close_prices]
#                             linechart = ui.echart({
#                                 'xAxis': {
#                                     'type': 'category',
#                                     'data': dates,  # Fechas
#                                     'axisLabel': {'fontSize': 10}
#                                 },
#                                 'yAxis': {
#                                     'type': 'value'
#                                 },
#                                 'series': [{
#                                     'data': formatted_close_prices,  
#                                     'type': 'line',
#                                     'smooth': True,
#                                     'areaStyle': {'color': 'rgba(0, 112, 243, 0.2)'},
#                                     'lineStyle': {'color': '#0070F3', 'width': 3}
#                                 }],
#                                 'tooltip': {
#                                     'trigger': 'axis'
#                                 }
#                             }).classes('w-80 h-60 rounded-lg shadow-sm') 
#                     else:
#                         ui.label("No disponible").classes('text-center text-gray-500')

#             # Segunda fila con una sola columna para las pestañas
#             with ui.row().classes('w-full mt-6'):
#                 with ui.column().classes('w-full'):
#                     # Crear las pestañas
#                     with ui.tabs().classes('mb-4 w-full') as tabs:
#                         # Definir las pestañas
#                         pl = ui.tab('Información básica')  
#                         bl = ui.tab('Precio')  
#                         cf = ui.tab('Datos financieros')  

#                     # Establecer cuál será la pestaña activa por defecto
#                     with ui.tab_panels(tabs, value=pl):
#                         # Panel de Información general
#                         with ui.tab_panel(pl).classes('bg-blue-50 p-4 rounded-lg shadow-lg'):
#                             with ui.column().classes('gap-4'):
#                                 ui.label(f"Nombre: {info_ticker.company_name}").classes('text-xl text-blue-800 font-semibold')
#                                 ui.label(f"Símbolo: {info_ticker.symbol}").classes('text-lg text-gray-700')
#                                 ui.label(f"Sector industrial: {info_ticker.sector}").classes('text-lg text-gray-700')
#                                 ui.label(f"Industria: {info_ticker.industry}").classes('text-lg text-gray-700')
#                                 ui.label(f"País: {info_ticker.country}").classes('text-lg text-gray-700')
#                                 ui.label(f"Empleados a tiempo completo: {info_ticker.full_time_employees}").classes('text-lg text-gray-700')
#                                 ui.label(f"Sitio web: {info_ticker.website}").classes('text-lg text-blue-500 underline')

#                         # Panel de Precios
#                         with ui.tab_panel(bl).classes('bg-blue-50 p-4 rounded-lg shadow-lg'):
#                             if price_data:
#                                 price = price_data[0]
#                                 ui.label(f"Símbolo: {price.symbol}").classes('text-xl text-blue-800 font-semibold')
#                                 ui.label(f"Variación diaria: {price.day:,.2f}%").classes('text-lg text-green-700' if price.day >= 0 else 'text-red-700')
#                                 ui.label(f"Variación semanal: {price.week:,.2f}%").classes('text-lg text-green-700' if price.week >= 0 else 'text-red-700')
#                                 ui.label(f"Variación mensual: {price.month:,.2f}%").classes('text-lg text-green-700' if price.month >= 0 else 'text-red-700')
#                                 ui.label(f"Variación anual: {price.year:,.2f}%").classes('text-lg text-green-700' if price.year >= 0 else 'text-red-700')

#                         # Panel de Datos financieros
#                         with ui.tab_panel(cf).classes('bg-blue-50 p-4 rounded-lg shadow-lg'):
#                             with ui.column().classes('gap-4'):
#                                 ui.label(f"Capitalización de mercado: ${info_ticker.market_cap:,.2f}").classes('text-xl text-blue-800 font-semibold')
#                                 ui.label(f"Precio actual: ${info_ticker.current_price:,.2f}").classes('text-lg text-gray-700')
#                                 ui.label(f"Cierre anterior: ${info_ticker.previous_close:,.2f}").classes('text-lg text-gray-700')
#                                 ui.label(f"Dividendos: {info_ticker.dividend_yield}%").classes('text-lg text-gray-700')
#                                 ui.label(f"Ingresos totales: ${info_ticker.total_revenue:,.2f}").classes('text-lg text-gray-700')
#                                 ui.label(f"Ingreso neto: ${info_ticker.net_income:,.2f}").classes('text-lg text-gray-700')
#                                 ui.label(f"Flujo de caja libre: ${info_ticker.free_cashflow:,.2f}").classes('text-lg text-gray-700')
#                                 ui.label(f"Rentabilidad sobre activos: {info_ticker.return_on_assets:,.3f}%").classes('text-lg text-gray-700')
#                                 ui.label(f"Rentabilidad sobre el capital: {info_ticker.return_on_equity:,.3f}%").classes('text-lg text-gray-700')
#                                 ui.label(f"Deuda sobre capital: {info_ticker.debt_to_equity:,.3f}").classes('text-lg text-gray-700')
#                                 ui.label(f"Ratio rápido: {info_ticker.quick_ratio:,.3f}").classes('text-lg text-gray-700')
#                                 ui.label(f"Ratio corriente: {info_ticker.current_ratio:,.3f}").classes('text-lg text-gray-700')
from datetime import datetime, timedelta

# Método para actualizar el gráfico según el filtro seleccionado
def update_price_chart(ticker: str, period: str, price_data: list, historical_data: list, chart_container):
    """Actualiza el gráfico con el periodo seleccionado y muestra la variación correspondiente"""
    
    # Limpiar el contenedor antes de agregar nuevos elementos
    chart_container.clear()  # Asegúrate de que el contenedor se limpie antes de agregar el nuevo gráfico

    if price_data:
        price = price_data[0]  # Accedemos al primer objeto de la lista price_data
        
        # Determina el número de días a mostrar según el periodo seleccionado
        now = datetime.now()
        
        if period == "1M":
            days = 30
            variation = price.day  # Variación diaria
            label = f"Variación diaria: {price.day:,.2f}%"
        elif period == "3M":
            days = 90
            variation = price.week  # Variación semanal
            label = f"Variación semanal: {price.week:,.2f}%"
        elif period == "6M":
            days = 180
            variation = price.month  # Variación mensual
            label = f"Variación mensual: {price.month:,.2f}%"
        elif period == "1A":
            days = 365
            variation = price.year  # Variación anual
            label = f"Variación anual: {price.year:,.2f}%"
        elif period == "YTD":
            start_of_year = datetime(now.year, 1, 1)
            days = (now - start_of_year).days
            variation = price.year  # Usar la variación anual
            label = f"Variación anual (YTD): {price.year:,.2f}%"
        elif period == "5A":
            days = 365 * 5
            variation = price.year  # Variación anual
            label = f"Variación anual (5 años): {price.year:,.2f}%"
        else:
            days = 365  # Fallback
            variation = price.year  # Variación anual
            label = f"Variación anual: {price.year:,.2f}%"

        # Filtrar los datos históricos según el periodo
        filtered_data = historical_data[-days:]
        
        if filtered_data:
            dates = [data.date for data in filtered_data]
            close_prices = [data.close for data in filtered_data]
        else:
            dates = []
            close_prices = []

        # Crear el gráfico actualizado
        formatted_close_prices = [f"{price:.2f}" for price in close_prices]
        
        # Crear el gráfico en la interfaz
        line_chart = ui.echart({
            'xAxis': {
                'type': 'category',
                'data': dates,  # Fechas filtradas
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
        }).classes('w-80 h-60 rounded-lg shadow-sm')

        # Mostrar la variación correspondiente en la interfaz de usuario
        ui.label(label).classes('text-lg ' + ('text-green-700' if variation >= 0 else 'text-red-700')).classes('mt-4').append_to(chart_container)

        # Actualizar el gráfico en el contenedor
        line_chart.update()
    else:
        # Si no hay datos de price_data, mostrar un mensaje de error
        ui.label("Datos de variación no disponibles").classes('text-red-700').append_to(chart_container)

class Main:
    def __init__(self) -> None:
        tickers = ['AMZN', 'GOOGL', 'META', 'TSLA', 'NVDA', 'NFLX']
        self.cache = Cache()  # Usamos la caché en memoria
        
        @ui.page('/')
        def create_stock_cards(client: Client):
            client.layout.classes(Colors.body)
            Layout()

            with ui.row().classes('grid grid-cols-2 gap-4 mx-auto w-full px-2 justify-evenly'):
                for i in range(2):  # Primeras dos tarjetas
                    with ui.column().classes('w-full'):
                        self.create_stock_card(client, tickers[i])

    
    def fetch_data_from_api(self, ticker: str):
        """Simula la llamada a la API para obtener datos"""
        yahoo_historical = YahooFinanceHistorical()
        historical_data = yahoo_historical.get_historical_data(ticker, period="1y")
        return historical_data
    
    
    def get_stock_data(self, ticker: str):
        """Obtiene los datos del stock, utilizando la caché si es posible"""
        cached_data = self.cache.get(ticker)
        
        if cached_data:
            print(f"Usando datos de caché para {ticker}")
            return cached_data
        else:
            # Si no hay datos en caché, obtener desde la API
            data = self.fetch_data_from_api(ticker)
            self.cache.set(ticker, data)  # Guardamos los datos en la caché
            return data

    
    
    
    def create_stock_card(self, client: Client, ticker: str, period: str = "1y"):
        try:
            historical_data = self.get_stock_data(ticker)  # Datos históricos
            api_fmp = AssetsAPI(fmp_api_key='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4')
            yahoo_info = YahooFinanceInfo()
            info_ticker = yahoo_info.get_info(ticker)
            company_name = info_ticker.company_name if info_ticker else "N/A"
            
            # Fechas y precios de cierre para el gráfico
            dates = [data.date for data in historical_data] if historical_data else []
            close_prices = [data.close for data in historical_data] if historical_data else []
            
            api = AssetsAPI(fmp_api_key='4Y2glVed0qPOPExJM2Hrj2f4mUPUSPPP')
            price_data = api.fmp.price.change(ticker)

        except Exception as e:
            print(f"Error: {e}")
            return
        
        with ui.card().classes('w-full p-6 rounded-xl shadow-lg bg-blue-50'):
            with ui.row().classes('flex gap-7'):
                with ui.column().classes('flex-1'):
                    ui.label(company_name).classes('text-3xl text-gray-800 text-left font-semibold')
                    ui.label(f'({ticker})').classes('text-sm font-medium text-gray-500')
                    if historical_data:
                        ui.label(f'${historical_data[0].close:,.2f}').classes('text-4xl text-right font-extrabold text-gray-800')
                    else:
                        ui.label(f'No disponible').classes('text-4xl text-right font-extrabold text-gray-800')

                with ui.column().classes('flex-none w-52 h-aut'):
                    if historical_data:
                        formatted_close_prices = [f"{price:.2f}" for price in close_prices]
                        linechart = ui.echart({
                            'xAxis': {
                                'type': 'category',
                                'data': dates,  # Fechas
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
                        }).classes('w-80 h-60 rounded-lg shadow-sm')
                    else:
                        ui.label("No disponible").classes('text-center text-gray-500')

            ui.separator().classes('my-8 border-gray-300')

            # Crear las pestañas
            with ui.row().classes('w-full mt-6'):
                with ui.column().classes('w-full'):
                    with ui.tabs().classes('mb-0 w-full').style('border-bottom: 2px solid #e2e8f0') as tabs:
                        pl = ui.tab('Información básica')
                        bl = ui.tab('Precio')
                        cf = ui.tab('Datos Financieros')

                    # Aquí estamos usando el `value` para controlar cuál panel está activo.
                    with ui.tab_panels(tabs, value=bl):  # La pestaña activa es la de 'Precio' al principio
                        # Panel de Información básica
                        with ui.tab_panel(pl).classes('bg-blue-50'):
                            with ui.column().classes('gap-2 p-4 rounded-lg shadow-sm w-80'):
                                ui.label(f"Nombre: {info_ticker.company_name}").classes('text-base text-gray-700')
                                ui.label(f"Símbolo: {info_ticker.symbol}").classes('text-base text-gray-700')
                                ui.label(f"Sector: {info_ticker.sector}").classes('text-base text-gray-700')
                                ui.label(f"Industria: {info_ticker.industry}").classes('text-base text-gray-700')
                                ui.label(f"País: {info_ticker.country}").classes('text-base text-gray-700')

                        # Panel de Precios
                        with ui.tab_panel(bl).classes('bg-blue-50 p-2 rounded-lg shadow-lg'):
                            # Define el contenedor para el gráfico
                            with ui.column():
                            # Botones de filtro
                                with ui.row().classes('w-full justify-center gap-2') as filter_buttons:  # Los botones estarán en fila
                                    for period in ["1M", "3M", "6M", "1A", "YTD"]:  # Se eliminó "5A"
                                        ui.button(period, on_click=lambda p=period: update_price_chart(ticker, p, price_data, historical_data)) \
                                            .classes('bg-white text-black font-semibold px-4 py-2 rounded-lg shadow-sm')  # Estilo de los botones


                            with ui.column():
                                linechart = ui.echart({
                                    'xAxis': {
                                        'type': 'category',
                                        'data': dates,  # Fechas filtradas
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
                                }).classes('w-80 h-60 rounded-lg shadow-sm')

                        # Panel de Datos Financieros
                        with ui.tab_panel(cf).classes('bg-blue-50 p-4 rounded-lg shadow-lg'):
                            with ui.column().classes('gap-2 p-4 rounded-lg shadow-sm w-80'):
                                ui.label(f"Capitalización de mercado: ${info_ticker.market_cap:,.2f}").classes('text-base text-gray-700')
                                ui.label(f"Precio actual: ${info_ticker.current_price:,.2f}").classes('text-base text-gray-700')
                                ui.label(f"Cierre anterior: ${info_ticker.previous_close:,.2f}").classes('text-base text-gray-700')
                                ui.label(f"Dividendos: {info_ticker.dividend_yield}%").classes('text-base text-gray-700')
                                ui.label(f"Ingresos totales: ${info_ticker.total_revenue:,.2f}").classes('text-base text-gray-700')

