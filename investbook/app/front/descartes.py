# from __future__ import annotations

# from nicegui import ui, Client

# from investbook.sources import AssetsAPI

# from datetime import datetime

# from investbook.app.front.shared.layout import Layout

# from investbook.app.front.shared.colors import Colors
# from investbook.app.front.components.searchbar import (
#     SearchBar,
#     SearchStyle,
#     DataSet
# )

# class Main:

#     def __init__(self) -> None:

#         @ui.page('/')
#         async def root(client: Client):

#             client.layout.classes(Colors.body)

#             Layout()

#             await self.search_bar
            
        


#             @ui.page('/yfinance/info') 
#             async def search_bar_info():
#                 info_data = []

#                 async def search_info(ticker: str):
#                     if ticker:
#                         ui.navigate.to(f"/yfinance/info/{ticker}")

            
#                 search_bar = SearchBar(
#                     title='Buscar Stocks',
#                     source_data=[
#                         DataSet(
#                             data=info_data, 
#                             field='symbol',  
#                             rt_prefix='price', 
#                             icon='search'
#                         )
#                     ],
#                     style=SearchStyle(
#                         color='blue',
#                         text_color='black',
#                         text_size_input='lg',
#                         text_size_results='md',
#                         round_size='3xl',
#                         icon_size='sm'
#                     ),
#                     max_search=8
#                 )

#                 with ui.row().classes('mt-4 items-center space-x-4'):  
#                     search_bar

#                     ui.button('Buscar', on_click=lambda: search_info(search_bar.search_bar.value)).classes('bg-blue-500 text-white px-6 py-2 rounded-lg')

#                 return search_bar
            
            
#             @ui.page('/yfinance/historical') 
#             async def search_bar_info():
#                 info_data = []

#                 async def search_ynfo(ticker: str):
#                     if ticker:
#                         ui.navigate.to(f"/yfinance/historical/{ticker}")

            
#                 search_bar = SearchBar(
#                     title='Buscar histórico de datos',
#                     source_data=[
#                         DataSet(
#                             data=info_data, 
#                             field='symbol',  
#                             rt_prefix='price', 
#                             icon='search'
#                         )
#                     ],
#                     style=SearchStyle(
#                         color='blue',
#                         text_color='black',
#                         text_size_input='lg',
#                         text_size_results='md',
#                         round_size='3xl',
#                         icon_size='sm'
#                     ),
#                     max_search=8
#                 )

#                 with ui.row().classes('mt-4 items-center space-x-4'):  
#                     search_bar

#                     ui.button('Buscar', on_click=lambda: search_ynfo(search_bar.search_bar.value)).classes('bg-blue-500 text-white px-6 py-2 rounded-lg')

#                 return search_bar
                
            
                
                
                
#             @ui.page('/polygon/indices') 
#             async def search_bar_indices():
#                 indices_data = []

#                 async def search_in(search_text: str, search_date: str):
#                     if search_text and search_date:
#                         ui.navigate.to(f"/polygon/indices/{search_text}/{search_date}")

#                 ui.label("Esta solicitud devuelve el precio de apertura, de cierre, el precio máximo y mínimo de los tickers disponibles de los índices en la fecha indicada"
#                 ).classes('mb-4 text-lg text-gray-700').style('font-weight: bold')
                
#                 search_bar = SearchBar(
#                     title='Buscar Índice',
#                     source_data=[
#                         DataSet(
#                             data=indices_data, 
#                             field='symbol',  
#                             rt_prefix='price', 
#                             icon='search'
#                         )
#                     ],
#                     style=SearchStyle(
#                         color='blue',
#                         text_color='black',
#                         text_size_input='lg',
#                         text_size_results='md',
#                         round_size='3xl',
#                         icon_size='sm'
#                     ),
#                     max_search=8
#                 )

#                 with ui.row().classes('mt-4 items-center space-x-4'):  
#                     search_bar

#                     ui.label('Fecha:').classes('mr-2')  
#                     date_picker = ui.input(
#                         placeholder='YYYY-MM-DD',
#                         value=datetime.now().strftime('%Y-%m-%d')  # Fecha actual por defecto
#                     ).classes('w-32')

#                     ui.button('Buscar', on_click=lambda: search_in(search_bar.search_bar.value, date_picker.value)).classes('bg-blue-500 text-white px-6 py-2 rounded-lg')

#                 return search_bar

                    
                
            
#             @ui.page('/polygon/cryptos')
#             async def search_bar_cryptos():
#                 indices_data = []

#                 async def search_crypto(crypto: str, currency: str, date: str):
#                     if crypto and currency and date:
#                         ui.navigate.to(f"/polygon/cryptos/{crypto}/{currency}/{date}")

#                 ui.label("Esta solicitud devuelve el precio de apertura y de cierre de los tickers disponibles de criptomonedas en la fecha indicada"
#                 ).classes('mb-4 text-lg text-gray-700').style('font-weight: bold')
                
#                 search_bar = SearchBar(
#                     title='Buscar Criptomoneda',
#                     source_data=[
#                         DataSet(
#                             data=indices_data, 
#                             field='symbol',  
#                             rt_prefix='price', 
#                             icon='search'
#                         )
#                     ],
#                     style=SearchStyle(
#                         color='blue',
#                         text_color='black',
#                         text_size_input='lg',
#                         text_size_results='md',
#                         round_size='3xl',
#                         icon_size='sm'
#                     ),
#                     max_search=8
#                 )

#                 # Crea el campo para seleccionar la divisa
#                 with ui.row().classes('mt-4 items-center space-x-4'):  
#                         search_bar
                        
#                         ui.label('Divisa:').classes('mr-2')  
#                         currency_input = ui.input(
#                             placeholder='USD',
#                             value='USD'  # Establece USD como valor por defecto
#                         ).classes('w-32')

#                         ui.label('Fecha:').classes('mr-2')  
#                         date_picker = ui.input(
#                             placeholder='YYYY-MM-DD',
#                             value=datetime.now().strftime('%Y-%m-%d')  
#                         ).classes('w-32')

#                         ui.button('Buscar', on_click=lambda: search_crypto(search_bar.search_bar.value, currency_input.value, date_picker.value)).classes('bg-blue-500 text-white px-6 py-2 rounded-lg')

#                         return search_bar
                

#             @ui.page('/polygon/stocks') 
#             async def search_bar_stocks():
#                 stocks_data = []

                
#                 async def search_st(search_text: str, search_date: str):
#                     if search_text and search_date:
#                         ui.navigate.to(f"/polygon/stocks/{search_text}/{search_date}")

                
#                 ui.label("Esta solicitud devuelve el precio de apertura, de cierre, el precio máximo, mínimo y el volumen de los tickers disponibles de los stocks en la fecha indicada"
#                 ).classes('mb-4 text-lg text-gray-700').style('font-weight: bold')
                
#                 search_bar = SearchBar(
#                     title='Buscar Acción',
#                     source_data=[
#                         DataSet(
#                             data=stocks_data, 
#                             field='symbol',  
#                             rt_prefix='price', 
#                             icon='search'
#                         )
#                     ],
#                     style=SearchStyle(
#                         color='blue',
#                         text_color='black',
#                         text_size_input='lg',
#                         text_size_results='md',
#                         round_size='3xl',
#                         icon_size='sm'
#                     ),
#                     max_search=8
#                 )

#                 # Crea el campo para seleccionar la fecha
#                 with ui.row().classes('mt-4'):
#                     ui.label('Selecciona la fecha').classes('mr-2')
#                     date_picker = ui.input(
#                         label='Fecha',
#                         placeholder='YYYY-MM-DD',
#                         value=datetime.now().strftime('%Y-%m-%d')  # Establece la fecha actual por defecto
#                     ).classes('w-32')

#                 with ui.column().classes('justify-right mt-4'):
#                     ui.button('Buscar', on_click=lambda: search_st(search_bar.search_bar.value, date_picker.value)).classes('bg-blue-500 text-white px-6 py-2 rounded-lg text-right')

#                 return search_bar




#         @ui.page('/finhub/info') 
#         async def search_bar_info(client: Client):
#                 info = []
                
#                 async def search_st(ticker: str):
#                     if ticker:
#                         ui.navigate.to(f"/finhub/info/{ticker}")

                
#                 ui.label("Esta solicitud devuelve los datos básicos de la empresa junto con los datos de cotización de la última sesión públicada y una recomendación de compra/venta"
#                 ).classes('mb-4 text-lg text-gray-700').style('font-weight: bold')
                
#                 search_bar = SearchBar(
#                     title='Buscar Acción',
#                     source_data=[
#                         DataSet(
#                             data=info, 
#                             field='symbol',  
#                             rt_prefix='price', 
#                             icon='search'
#                         )
#                     ],
#                     style=SearchStyle(
#                         color='blue',
#                         text_color='black',
#                         text_size_input='lg',
#                         text_size_results='md',
#                         round_size='3xl',
#                         icon_size='sm'
#                     ),
#                     max_search=8
#                 )

                
#                 with ui.row().classes('mt-4 items-center space-x-4'):  
#                     search_bar

#                     ui.button('Buscar', on_click=lambda: search_st(search_bar.search_bar.value)).classes('bg-blue-500 text-white px-6 py-2 rounded-lg')

#                 return search_bar
            


                    
                
#         @property
#         async def search_bar(self):
#             stocks = []
#             try:
#                 api=AssetsAPI(fmp_api_key='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4')
#                 stocks = api.fmp.stock.list()
#             except Exception as e:
#                 print(e)


#             return SearchBar(
#                 title='Stocks',
#                 source_data=[
#                     DataSet(
#                         data=stocks,  
#                         field='symbol',  
#                         rt_prefix='stocks',
#                         icon='search'
#                     )
#                 ],
#                 style=SearchStyle(
#                     color='blue',
#                     text_color='black',
#                     text_size_input='lg',
#                     text_size_results='md',
#                     round_size='3xl',
#                     icon_size='sm'
#                 ),
#                 max_search=8
#             )
        
    
#         @ui.page('/fmp/price') 
#         async def search_bar_price():
#             price = []
            
#             async def search_price(ticker:str):
#                 if ticker: 
#                     ui.navigate.to(f"/fmp/price/{ticker}")


#             ui.label("Esta solicitud devuelve una lista con el precio del ticker busacdo en diferentes rangos de tiempo"
#                 ).classes('mb-4 text-lg text-gray-700').style('font-weight: bold')
            
#             search_bar = SearchBar(
#                 title='Buscar Acción',
#                 source_data=[
#                     DataSet(
#                         data=price, 
#                         field='symbol',  
#                         rt_prefix='price', 
#                         icon='search'
#                     )
#                 ],
#                 style=SearchStyle(
#                     color='blue',
#                     text_color='black',
#                     text_size_input='lg',
#                     text_size_results='md',
#                     round_size='3xl',
#                     icon_size='sm'
#                 ),
#                 max_search=8
#             )
            
#             with ui.row().classes('mt-4 items-center space-x-4'):  
#                 search_bar  

#                 ui.button('Buscar', on_click=lambda: search_price(search_bar.search_bar.value)).classes('bg-blue-500 text-white px-6 py-2 rounded-lg')

#             return search_bar
                






#         @ui.page('/fmp/company') 
#         async def search_bar_company():
#             company = []
            
#             async def search_company(ticker:str):
#                 if ticker: 
#                     ui.navigate.to(f"/fmp/company/{ticker}")


#             ui.label("Esta solicitud devuelve una lista con toda la información básica del ticker, como la capitalización de mercado, el número de empleados..."
#                 ).classes('mb-4 text-lg text-gray-700').style('font-weight: bold')
            
#             search_bar = SearchBar(
#                 title='Buscar Acción',
#                 source_data=[
#                     DataSet(
#                         data=company, 
#                         field='symbol',  
#                         rt_prefix='company', 
#                         icon='search'
#                     )
#                 ],
#                 style=SearchStyle(
#                     color='blue',
#                     text_color='black',
#                     text_size_input='lg',
#                     text_size_results='md',
#                     round_size='3xl',
#                     icon_size='sm'
#                 ),
#                 max_search=8
#             )

                
#             with ui.row().classes('mt-4 items-center space-x-4'):  
#                 search_bar  

#                 ui.button('Buscar', on_click=lambda: search_company(search_bar.search_bar.value)).classes('bg-blue-500 text-white px-6 py-2 rounded-lg')

#             return search_bar
                

#         @ui.page('/fmp/financials') 
#         async def search_bar_financials():
#             financials = []
#             async def search_fin(ticker:str):
#                     if ticker: 
#                         ui.navigate.to(f"/fmp/financials/{ticker}")

#             ui.label("Esta solicitud devuelve una lista con el acceso en tiempo real a los datos de la cuenta de resultados del ticker."
#                 ).classes('mb-4 text-lg text-gray-700').style('font-weight: bold')
            
#             search_bar = SearchBar(
#                 title='Buscar Acción',
#                 source_data=[
#                     DataSet(
#                         data=financials, 
#                         field='symbol',  
#                         rt_prefix='financials', 
#                         icon='search'
#                     )
#                 ],
#                 style=SearchStyle(
#                     color='blue',
#                     text_color='black',
#                     text_size_input='lg',
#                     text_size_results='md',
#                     round_size='3xl',
#                     icon_size='sm'
#                 ),
#                 max_search=8
#             )
            
#             with ui.row().classes('mt-4 items-center space-x-4'):  
#                 search_bar  

#                 ui.button('Buscar', on_click=lambda: search_fin(search_bar.search_bar.value)).classes('bg-blue-500 text-white px-6 py-2 rounded-lg')

#             return search_bar
        

#         @ui.page('/fmp/dividends') 
#         async def search_bar_dividends():
            
#             dividends = []
            
#             async def search_dividends(ticker:str):
#                         if ticker: 
#                             ui.navigate.to(f"/fmp/dividends/{ticker}")

#             ui.label("Esta solicitud devuelve una lista con los datos del último dividendo pagado del ticker a los socios."
#                 ).classes('mb-4 text-lg text-gray-700').style('font-weight: bold')
            
#             search_bar = SearchBar(
#                 title='Buscar Dividendos',
#                 source_data=[
#                     DataSet(
#                         data=dividends, 
#                         field='symbol',  
#                         rt_prefix='dividends', 
#                         icon='search'
#                     )
#                 ],
#                 style=SearchStyle(
#                     color='blue',
#                     text_color='black',
#                     text_size_input='lg',
#                     text_size_results='md',
#                     round_size='3xl',
#                     icon_size='sm'
#                 ),
#                 max_search=8
#             )
                
#             with ui.row().classes('mt-4 items-center space-x-4'):  
#                 search_bar  

#                 ui.button('Buscar', on_click=lambda: search_dividends(search_bar.search_bar.value)).classes('bg-blue-500 text-white px-6 py-2 rounded-lg')

#             return search_bar
                
