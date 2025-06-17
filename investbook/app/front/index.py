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
    
    def __init__(self, file_path="investbook/app/front/images/usuarios.json"):
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
          
#Esta clase es la que usamos para cambiar el color de los botones de los filtros
class ToggleButton(ui.button):
    buttons = []  # Lista para almacenar los botones

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.clicked = False # Marcamos que los botones están desmarcados
        ToggleButton.buttons.append(self)  # Agregar el botón a la lista
        self.on('click', self.toggle)

    def toggle(self) -> None:
        """Toggle the button state."""
        # Primero, ponemos todos los botones en blanco
        for btn in ToggleButton.buttons:
            if btn != self:
                btn.clicked = False
                btn.props(f'color=white')  # Volver a blanco a los otros botones

        # Luego, cambiamos el estado del botón clicado
        self.clicked = not self.clicked
        new_color = "grey" if self.clicked else "white"
        self.props(f'color={new_color}')  # Cambiar color del botón actual
        super().update()  # Actualizar el botón



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

            with ui.row().classes('justify-center items-center h-screen w-full p-4'):
                with ui.card().classes(
                    'shadow-lg rounded-lg bg-gradient-to-r from-[#5898d4] to-[#88c5e9] text-white '
                    'p-8 flex md:flex-row md:space-x-10 md:items-start '
                    'sm:flex-col sm:space-y-6 sm:w-full sm:max-w-md sm:p-6'
                ):
                    with ui.row().classes('justify-between items-start md:flex-row sm:flex-col sm:items-center sm:text-center'):
                        with ui.column().classes('items-left text-left md:mr-40 sm:items-center sm:text-center'):
                            ui.image("investbook/app/front/images/logo2.png").classes("w-64 mb-6 sm:w-40")  
                            ui.label('Iniciar sesión').classes('text-4xl font-semibold md:text-4xl sm:text-2xl')  # Texto más grande solo en PC

                        with ui.column().classes('text-white space-y-4 w-full'):
                            usuario_input = ui.input(label="Usuario").classes(
                                'w-full text-white border-b-2 border-white bg-transparent font-semibold'
                            )
                            contrasena_input = ui.input(label="Contraseña", password=True).classes(
                                'w-full text-white border-b-2 border-white bg-transparent font-bold'
                            )

                            ui.button('Iniciar sesión', on_click=lambda: self.login_user(client, usuario_input.value, contrasena_input.value)).classes(
                                'bg-orange-500 text-white px-6 py-3 rounded-lg shadow-lg hover:bg-orange-400 transition duration-300 ease-in-out '
                                'sm:w-full sm:px-4 sm:py-2'
                            )

                            
                            
        @ui.page('/')
        def create_stock_cards(client: Client):
            if not self.usuario_actual:  
                ui.navigate.to('/login')
                return  
            
            tickers = self.login.obtener_tickers(self.usuario_actual)
            
            client.layout.classes(Colors.body)
            Layout(self.usuario_actual)
            
            stocks = []
            selected_stock = [None]  
            
                
            async def check_stocks():
                try:
                    api = AssetsAPI(fmp_api_key='qd8qbTjUzah8tDi3mwM1MaDeskOanjwy')
                    data = api.fmp.stock.list()
                    return [s.symbol for s in data]  
                except Exception as e:
                    print(e)
                    return []

            async def update_search(event):
                query = event.value.lower()
                if not query:
                    results_container.clear()
                    return

                if not stocks:
                    stocks.extend(await check_stocks())  
                results = [s for s in stocks if query in s.lower()][:3]  

                results_container.clear() 
                with results_container:
                    for stock in results:
                        ui.button(stock, on_click=lambda s=stock: select_stock(s))


            def select_stock(stock):
                search_input.set_value(stock)  # Establecer el valor seleccionado en el input
                selected_stock[0] = stock  
                results_container.clear()  # Limpiar los resultados mostrados
                if selected_stock[0]:
                    self.add_ticker_to_user(selected_stock[0])  
                search_input.set_value('')  # Limpiar el input
                search_input.set_placeholder('Buscar stock...')  # Restablecer el placeholder
                results_container.clear()  # Limpiar el contenedor de resultados


            with ui.row().classes("w-full justify-end items-center"): 
                with ui.column().classes("relative w-48"):  # Contenedor relativo para posicionar el results_container
                    search_input = ui.input(
                        placeholder="Buscar stock...",
                        on_change=update_search
                    ).classes("text-xl w-full")

                    results_container = ui.column().classes(
                        "text-center items-left absolute top-full left-0 rounded-lg w-full z-10 mt-2 border-4"
                    ).style(
                        "background-color: #e5ecf5; max-height: 299px; overflow-y: auto; padding: 5px;"
                    )

                ui.button('Buscar', on_click=select_stock).classes(
                    'bg-blue-500 text-white px-4 py-2 rounded-lg shadow-lg hover:bg-blue-400 ml-4'
    )



            
            with ui.row().classes('grid grid-cols-1 md:grid-cols-2 gap-10 mx-auto w-full justify-evenly').style('padding-left: 30px; padding-right: 30px;') as self.card_container:

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
                'grid': {
                    'left': '18%',  # Aumentamos el margen izquierdo para que los números sean visibles
                    'right': '5%',
                    'top': '10%',
                    'bottom': '15%'
                },
                'xAxis': {
                    'type': 'category',
                    'data': dates,
                    'axisLabel': {'fontSize': 8}
                },
                'yAxis': {
                    'type': 'value',
                    'name': 'Precio ($)',
                    'nameLocation': 'middle',
                    'nameTextStyle': {
                        'fontSize': 10,
                        'color': '#333',
                        'padding': [0, 0, 20, 0]
                    },
                    'axisLabel': {  # Ajustamos el tamaño de los números del eje Y
                        'fontSize': 10,  
                        'color': '#333'
                    }
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
            }).classes('w-full h-auto rounded-lg shadow-sm').style('width: 100%; min-height: 200px; height: 60vh; max-height: 400px;')  


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
                
                with ui.column().classes('text-center items-center'):
                    with ui.row():
                        ui.label("¿Quieres eliminar esta tarjeta?").classes("text-xl text-gray-900 font-semibold text-center items-center")
                    with ui.row():
                        with ui.column().classes("mt-6 gap-8 justify-between text-center items-center"):
                            ui.button("Eliminar",on_click=lambda: self.eliminar_ticker_and_delete(card, ticker, dialog)).classes("text-white rounded-xl items-center text-center")
                        with ui.column().classes("mt-6 gap-8 justify-between text-center items-center"):
                            ui.button("Atrás",on_click=lambda: dialog.close()).classes(" text-white rounded-xl items-center text-center")
        dialog.open()

        
    def eliminar_ticker_and_delete(self, card, ticker, dialog):
        self.eliminar_ticker(self.usuario_actual, ticker)  
        card.delete()  
        dialog.close()  
        ui.navigate.reload()
         

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
            company_name = info_ticker.company_name 
            
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
                                diferencia_porcentual = ((historical_data[-1].close - historical_data[-2].close) / historical_data[-2].close) * 100
                                ui.label(f'${historical_data[-1].close:,.2f}').classes('text-4xl text-right font-extrabold text-gray-800')
                                if diferencia_porcentual > 0:
                                    ui.label(f'+ {diferencia_porcentual:,.2f}%').classes('text-xl text-right text-green-500')  
                                else:
                                    ui.label(f'{diferencia_porcentual:,.2f}%').classes('text-xl text-right text-red-500')  
                            else:
                                ui.label(f'No disponible').classes('text-4xl text-right font-extrabold text-gray-800')

                            ui.button('Ver más datos', on_click=lambda: ui.navigate.to(f"/info/{ticker}"))
                            
                        with ui.column().classes('flex-1 w-full h-auto ml-0 md:ml-4 md:pl-10 flex justify-right items-right overflow-hidden'):  # Aquí agregamos overflow-hidden

                            if historical_data:
                                formatted_close_prices = [f"{price:.2f}" for price in close_prices]
                                chart = ui.echart({
                                    'xAxis': {
                                        'type': 'category',
                                        'data': dates,
                                        'axisLabel': {'fontSize': 8}
                                    },
                                    'yAxis': {
                                        'type': 'value',
                                        'axisLabel': {'fontSize': 8}
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
                                }).classes('w-full sm:w-full md:w-96 h-60 rounded-lg shadow-sm')  # Ajuste aquí: solo w-full en móvil
                            else:
                                ui.label("No disponible").classes('text-center text-gray-500')

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
                                                ToggleButton(period, on_click=lambda p=period: self.apply_filter(ticker, p, historical_data)).classes(
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
                                            with ui.column().classes('p-6 rounded-lg shadow-sm w-full sm:w-2/5'):  # En móviles, columna ocupará el 100% del ancho
                                                for article in news[:3]:
                                                    with ui.row().classes('w-full mb-2'):
                                                        ui.label(f"Título de la noticia: {article.headline}").classes('text-base text-gray-700 font-bold text-left')
                                                    with ui.row():
                                                        ui.link('Ver noticia', article.url).classes('text-blue-500 hover:underline')

                                            with ui.column().classes('p-6 rounded-lg shadow-sm w-full sm:w-2/5'):  # Lo mismo aquí, en móviles ocupará el 100%
                                                for article in news[3:6]:
                                                    with ui.row().classes('w-full mb-2'):
                                                        ui.label(f"Título de la noticia: {article.headline}").classes('text-base text-gray-700 font-bold text-left')
                                                    with ui.row():
                                                        ui.link('Ver noticia', article.url).classes('text-blue-500 hover:underline')

                                    else:
                                        ui.label("No hay noticias de esta empresa esta última semana").classes('text-base text-gray-700 font-semibold text-center w-full items-center')


