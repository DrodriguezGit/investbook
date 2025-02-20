from __future__ import annotations
import json
from nicegui import ui, Client
from investbook.sources.yfinance.historical import YahooFinanceHistorical
from investbook.sources import AssetsAPI
from investbook.app.front.shared.layout import Layout
from investbook.app.front.shared.colors import Colors
from datetime import datetime, timedelta
from investbook.sources.yfinance.info import YahooFinanceInfo  
from datetime import datetime, timedelta
from investbook.app.front.components.searchbar import (SearchBar,SearchStyle,DataSet)

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


class Login:
    
    def __init__(self, file_path="investbook/app/front/usuarios.json"):
        self.file_path = file_path

    def _load_data(self):
        """Carga los datos de los usuarios desde el archivo JSON."""
        with open(self.file_path, "r") as archivo:
            return json.load(archivo)

    def _save_data(self, datos):
        """Guarda los datos de los usuarios en el archivo JSON."""
        with open(self.file_path, "w") as archivo:
            json.dump(datos, archivo, indent=4)

    def verificar_login(self, usuario, contrasena):
        """Verifica si las credenciales de login son correctas."""
        datos_usuarios = self._load_data()
        for usuario_data in datos_usuarios["usuarios"]:
            if usuario_data["username"] == usuario and usuario_data["password"] == contrasena:
                return True
        return False

    def obtener_tickers(self, usuario):
        """Obtiene los tickers asociados a un usuario."""
        datos_usuarios = self._load_data()
        for usuario_data in datos_usuarios["usuarios"]:
            if usuario_data["username"] == usuario:
                return usuario_data["tickers"]
        return []

    def agregar_ticker(self, usuario, ticker):
        """Agrega un nuevo ticker a los datos del usuario."""
        datos_usuarios = self._load_data()
        for usuario_data in datos_usuarios["usuarios"]:
            if usuario_data["username"] == usuario:
                if ticker not in usuario_data["tickers"]:
                    usuario_data["tickers"].append(ticker)
        self._save_data(datos_usuarios)

    def eliminar_ticker(self, usuario, ticker):
        """Elimina un ticker de los datos del usuario."""
        datos_usuarios = self._load_data()
        for usuario_data in datos_usuarios["usuarios"]:
            if usuario_data["username"] == usuario and ticker in usuario_data["tickers"]:
                usuario_data["tickers"].remove(ticker)
        self._save_data(datos_usuarios)
          


class Main:
    def __init__(self) -> None:
        self.cache = Cache()
        self.charts = {}
        self.cards = []
        self.usuario_actual = None
        self.login = Login()
        
        tickers = self.login.obtener_tickers(self.usuario_actual)

        @ui.page('/login')
        def login(client: Client):
            client.layout.classes(Colors.body)
            
            with ui.row().classes('justify-center items-center h-screen w-full overflow-hidden'):
                with ui.card().classes('flex p-8 space-y-4 shadow-lg rounded-lg bg-gradient-to-r from-[#5898d4] to-[#88c5e9] text-white'):
                    with ui.row().classes('justify-between items-start'):
                        with ui.column().classes('mr-40 items-left text-left'):
                            ui.html('<img src="https://www.google.com/favicon.ico" class="w-8 mx-auto mb-4">') 
                            ui.label('Iniciar sesión').classes('text-4xl font-semibold text-center mb-4')  

                        with ui.column().classes('text-white space-y-4 '):
                            usuario_input = ui.input(label="Usuario").classes('w-full text-white border-b-2 border-white bg-transparent font-semibold')
                            contrasena_input = ui.input(label="Contraseña", password=True).classes('w-full text-white border-b-2 border-white bg-transparent font-bold')
                            
                            ui.button('Iniciar sesión', on_click=lambda: self.login_user(client, usuario_input.value, contrasena_input.value)).classes(
                                'bg-orange-500 text-white px-6 py-3 rounded-lg shadow-lg hover:bg-orange-400 transition duration-300 ease-in-out')
                            
                            
        @ui.page('/')
        def create_stock_cards(client: Client):
            if not self.usuario_actual:  
                ui.navigate.to('/login')
                return  
            
            tickers = self.login.obtener_tickers(self.usuario_actual)
            
            client.layout.classes(Colors.body)
            Layout()
            
            with ui.row().classes("w-full flex justify-center items-center"):
                ui.image("investbook1.png").classes("w-72")

                # ui.icon("bar_chart").classes("text-4xl ml-4")  
                
            with ui.row().classes("justify-end w-full pr-10"):
                search_input = ui.input().classes("text-xl")
                ui.button('Buscar', on_click=lambda: self.add_ticker_to_user(search_input.value)).classes('bg-blue-500 text-white px-4 py-2 rounded-lg shadow-lg hover:bg-blue-400')


            
            with ui.row().classes('grid grid-cols-2 gap-10 mx-auto w-full justify-evenly').style('padding-left: 30px; padding-right: 30px;') as self.card_container:
                    for ticker in tickers:
                        self.create_stock_card(client, ticker)


    def add_ticker_to_user(self, ticker):
        
        self.login.agregar_ticker(self.usuario_actual, ticker)
        
        self.create_stock_card(self.usuario_actual, ticker)
        

    def login_user(self, client: Client, usuario, contrasena):
        if self.login.verificar_login(usuario, contrasena):
            self.usuario_actual = usuario
            
            ui.navigate.to('/')
        else:
            ui.label("Credenciales incorrectas").classes('text-red-500')


    def e_chart(self, ticker: str, period: str, historical_data: list):
        if historical_data:
            days = {
                "1 Semana": 7,
                "1 Mes": 30,
                "3 Meses": 90,
                "6 Meses": 180,
                "1 Año": 365
            }.get(period, 365)

            filtered_data = historical_data[-days:]
            
            dates = [data.date for data in filtered_data]
            close_prices = [data.close for data in filtered_data]

            return ui.echart({
                'xAxis': {
                    'type': 'category',
                    'data': dates,
                    'axisLabel': {'fontSize': 10}
                },
                'yAxis': {
                    'type': 'value',
                    'name': 'Precio ($)',  
                    'nameLocation': 'middle',  
                    'nameTextStyle': {
                        'fontSize': 12,
                        'color': '#333',
                        'padding': [0, 0, 20, 0]}
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
        chart = self.charts.get(ticker)
        if chart:
            try:
                if chart in chart.parent_slot.children:
                    chart.delete()
            except ValueError:
                print(f"El gráfico para {ticker} no se encuentra en la lista de hijos para eliminarlo.")

        days = {
            "1 Semana": 7,
            "1 Mes": 30,
            "3 Meses": 90,
            "6 Meses": 180,
            "1 Año": 365
        }.get(period, 365)

        filtered_data = historical_data[-days:]
        
        new_chart_options = self.e_chart(ticker, period, filtered_data)

        self.charts[ticker] = new_chart_options


    def fetch_data_from_api(self, ticker: str):
        yahoo_historical = YahooFinanceHistorical()
        historical_data = yahoo_historical.get_historical_data(ticker, period="1y")
        return historical_data
    
    
    def eliminar_ticker(self, usuario, ticker):
        datos_usuarios = self.login._load_data()
        for usuario_data in datos_usuarios["usuarios"]:
            if usuario_data["username"] == usuario and ticker in usuario_data["tickers"]:
                usuario_data["tickers"].remove(ticker)
        self.login._save_data(datos_usuarios)
    
    
    def confirm_delete(self, card, ticker: str):
        #dialog hace que sea un pop-up
        with ui.dialog() as dialog:
            #estética de card
            with ui.card().classes("border-2 rounded-4xl bg-gray-100 p-8 w-96"):
                
                with ui.column():
                    with ui.row():
                        ui.label("¿Quieres eliminar esta tarjeta?").classes("text-xl text-gray-900 font-semibold text-center items-center")
                    with ui.row():
                        with ui.column().classes("mt-6 gap-8 justify-between"):
                            ui.button("Eliminar",on_click=lambda: self.eliminar_ticker_and_delete(card, ticker, dialog)).classes("text-white rounded-xl items-center text-center")
                        with ui.column().classes("mt-6 gap-8 justify-between"):
                            ui.button("Atrás",on_click=lambda: dialog.close()).classes(" text-white rounded-xl items-center text-center")
        dialog.open()

        
    def eliminar_ticker_and_delete(self, card, ticker, dialog):
        self.eliminar_ticker(self.usuario_actual, ticker)
        card.delete()
        dialog.close()


    def get_stock_data(self, ticker: str):
        cached_data = self.cache.get(ticker)

        if cached_data:
            print(f"Usando datos de caché para {ticker}")
            return cached_data
        else:
            data = self.fetch_data_from_api(ticker)
            self.cache.set(ticker, data)
            return data
        
        
    def create_stock_card(self, client: Client, ticker: str, period: str = "1y", prepend: bool = False):
        try:
            historical_data = self.get_stock_data(ticker)
            yahoo_info = YahooFinanceInfo()
            info_ticker = yahoo_info.get_info(ticker)
            company_name = info_ticker.company_name if info_ticker else "N/A"
            
            dates = [data.date for data in historical_data] if historical_data else []
            close_prices = [data.close for data in historical_data] if historical_data else []
            
            api = AssetsAPI(finhub_api_key='cuquo81r01qifa4sdpngcuquo81r01qifa4sdpo0')
            news = api.finhub.get_symbol.company_news(ticker)
            
        except Exception as e:
            print(f"Error: {e}")
            return

        with self.card_container:
            with ui.column().classes('w-full'):
                with ui.card().classes('w-full p-6 rounded-xl shadow-lg bg-blue-50') as card:
                    with ui.row().classes('flex justify-between'):
                        with ui.column().classes('flex-none w-52'):
                            ui.label(company_name).classes('text-3xl text-gray-800 text-left font-semibold').style('overflow-wrap: break-word; word-wrap: break-word; white-space: normal;')
                            ui.label(f'({ticker})').classes('text-sm font-medium text-gray-500')
                            if historical_data:
                                ui.label(f'${historical_data[-1].close:,.2f}').classes('text-4xl text-right font-extrabold text-gray-800')
                            else:
                                ui.label(f'No disponible').classes('text-4xl text-right font-extrabold text-gray-800')

                            ui.button('Ver más datos', on_click=lambda: ui.navigate.to(f"/info/{ticker}"))
                            
                        with ui.column().classes('flex-1 pl-56 w-52 h-auto ml-4'):
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
                            
                
                    ui.button(icon='delete', on_click=lambda: self.confirm_delete(card, ticker)).classes(
                        'absolute top-1 right-1 p-1 bg-blue-50 text-white hover:bg-gray-800 transition-all duration-200').style(
                        'width: 20px; height: 18px; border-radius: 8px; font-size: 12px;')



                    with ui.row().classes('w-full mt-6 '):
                        with ui.column().classes('w-full'):
                            with ui.tabs().classes('mb-0 w-full justify-center items-center').style('border-bottom: 2px solid #e2e8f0') as tabs:
                                pl = ui.tab('Información básica')
                                bl = ui.tab('Precio')
                                cf = ui.tab('Datos Financieros')
                                un = ui.tab('Últimas noticias')

                            with ui.tab_panels(tabs, value=bl).classes('w-full'):
                                with ui.tab_panel(pl).classes('bg-blue-50'):
                                    with ui.row().classes('w-full justify-start items-center'):
                                        ui.label(f"Nombre:").classes('text-base text-gray-700 font-bold')
                                        ui.label(f"{info_ticker.company_name}").classes('text-base text-gray-700')

                                    with ui.row().classes('w-full justify-start items-center'):
                                        ui.label(f"Símbolo:").classes('text-base text-gray-700 font-bold')
                                        ui.label(f"{info_ticker.symbol}").classes('text-base text-gray-700')

                                    with ui.row().classes('w-full justify-start items-center'):
                                        ui.label(f"Sector:").classes('text-base text-gray-700 font-bold')
                                        ui.label(f"{info_ticker.sector}").classes('text-base text-gray-700')

                                    with ui.row().classes('w-full justify-start items-center'):
                                        ui.label(f"Industria:").classes('text-base text-gray-700 font-bold')
                                        ui.label(f"{info_ticker.industry}").classes('text-base text-gray-700')

                                    with ui.row().classes('w-full justify-start items-center'):
                                        ui.label(f"País:").classes('text-base text-gray-700 font-bold')
                                        ui.label(f"{info_ticker.country}").classes('text-base text-gray-700')



                                
                                with ui.tab_panel(bl).classes('bg-blue-50 p-6 rounded-lg shadow-lg w-full'):
                                    with ui.column().classes('w-full gap-4 items-center'):
                                        with ui.row().classes('w-full justify-center gap-4'):
                                            for period in ["1 Semana", "1 Mes", "3 Meses", "6 Meses", "1 Año"]:
                                                ui.button(period, on_click=lambda p=period: self.apply_filter(ticker, p, historical_data)).classes(
                                                    'bg-white text-black font-semibold px-6 py-3 rounded-lg shadow-md hover:bg-gray-200')
                                       
                                        with ui.row().classes('w-full justify-center'):
                                            chart = self.charts.get(ticker)
                                            if chart and chart.parent_slot and chart in chart.parent_slot.children:
                                                chart.delete()
                                                self.e_chart(ticker, "1 Semana", historical_data)
                                        

                                with ui.tab_panel(cf).classes('bg-blue-50 p-4 rounded-lg shadow-lg'):
                                    with ui.column().classes('gap-2 p-4 rounded-lg shadow-sm w-full min-w-[350px]'):
                                        with ui.row().classes('w-full justify-start items-center'):
                                            ui.label(f"Capitalización de mercado:").classes('text-base text-gray-700 font-bold')
                                            ui.label(f"${info_ticker.market_cap:,.2f}").classes('text-base text-gray-700')

                                        with ui.row().classes('w-full justify-start items-center'):
                                            ui.label(f"Precio actual:").classes('text-base text-gray-700 font-bold')
                                            ui.label(f"${historical_data[-1].close:,.2f}").classes('text-base text-gray-700')

                                        with ui.row().classes('w-full justify-start items-center'):
                                            ui.label(f"Cierre anterior:").classes('text-base text-gray-700 font-bold')
                                            ui.label(f"${historical_data[-2].close:,.2f}").classes('text-base text-gray-700')

                                        with ui.row().classes('w-full justify-start items-center'):
                                            ui.label(f"Dividendos:").classes('text-base text-gray-700 font-bold')
                                            ui.label(f"{info_ticker.dividend_yield}%").classes('text-base text-gray-700')

                                        with ui.row().classes('w-full justify-start items-center'):
                                            ui.label(f"Ingresos totales:").classes('text-base text-gray-700 font-bold')
                                            ui.label(f"${info_ticker.total_revenue:,.2f}").classes('text-base text-gray-700')

                                            
                                            
                                with ui.tab_panel(un).classes('bg-blue-50 p-6 rounded-lg shadow-lg'):
                                    if news:
                                        with ui.row().classes('max-w-5xl w-full justify-center mx-auto gap-12'):
                                            with ui.column().classes('p-6 rounded-lg shadow-sm w-2/5'):
                                                for article in news[:3]:
                                                    with ui.row().classes('w-full mb-2'):
                                                        ui.label(f"Título de la noticia: {article.headline}").classes('text-base text-gray-700 font-bold text-left')
                                                    with ui.row():
                                                        ui.link('Ver noticia', article.url).classes('text-blue-500 hover:underline')

                                            with ui.column().classes('p-6 rounded-lg shadow-sm w-2/5'):
                                                for article in news[3:6]:
                                                    with ui.row().classes('w-full mb-2'):
                                                        ui.label(f"Título de la noticia: {article.headline}").classes('text-base text-gray-700 font-bold text-left')
                                                    with ui.row():
                                                        ui.link('Ver noticia', article.url).classes('text-blue-500 hover:underline')

                                    else:
                                        ui.label("No hay noticias de esta empresa esta última semana").classes('text-base text-gray-700 font-semibold text-center w-full items-center')

