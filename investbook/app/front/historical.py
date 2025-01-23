# from nicegui import ui, Client
# from investbook.sources.yfinance.historical import YahooFinanceHistorical  
# from investbook.sources import AssetsAPI  
# from investbook.app.front.shared.layout import Layout
# from investbook.app.front.shared.colors import Colors


# class HistoricalData:
    
#     def __init__(self) -> None:

#         @ui.page('/yfinance/historical/{ticker}')
#         async def root(client: Client, ticker: str, period: str = "1y"):

#             client.layout.classes(Colors.body)
#             Layout()

#             try:
#                 yahoo_historical = YahooFinanceHistorical()
#                 historical_data = yahoo_historical.get_historical_data(ticker, period)
                
#                 api_fmp = AssetsAPI(fmp_api_key='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4')
#                 price_data = api_fmp.fmp.price.change(ticker)  
                
#                 api_finhub=AssetsAPI(finhub_api_key='ct8pt19r01qpc9s002l0ct8pt19r01qpc9s002lg')
#                 info_trends = api_finhub.finhub.get_symbol.get_trends(ticker)

#             except Exception as e:
#                 print(f"Error: {e}")
            
            
#             with ui.card().classes('w-full max-w-lg p-6 rounded-xl shadow-lg bg-blue-50'):
#              if historical_data:
#                 ui.label(f"Datos históricos de la empresa {ticker}").style('font-weight: bold; margin-left: 20px')

#                 # Extraemos las fechas y los precios de cierre para graficar
#                 dates = [data.date for data in historical_data]
#                 close_prices = [data.close for data in historical_data]

                
#                 ui.echart({
#                     'xAxis': {'type': 'category', 
#                                 'data': dates,
#                                 'axisLabel': {
#                                     'margin': 20  
#                                 }
#                     },
#                     'yAxis': {
#                         'axisLabel': {
#                             ':formatter': 'value => "$" + value',
#                             'fontSize': 10,  
#                             },
#                         'splitLine': {'show': True },  
#                     },
#                     'series': [
#                         {'type': 'line',
#                         'data': close_prices, 
#                         'smooth': True,
#                         'symbol': 'none',  # Elimina los puntos de la línea
#                         'lineStyle': {
#                                 'color': '#47a7f5',
#                                 'width': 3}
#                         }
#                     ],
#                     'tooltip': {
#                         'trigger': 'axis'
#                        },
#                 })

#              else:
#                 ui.label("No se pudo obtener los datos históricos del ticker.")
                
            
#             with ui.row().style('display: flexible; justify-content: left; align-items: center; width: 100%'):

#                 with ui.column().style('width: 30%;'):
#                     with ui.card().style('padding: 20px; border: 1px solid #ccc; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); height: 300px;'):
#                         if price_data:
#                             price = price_data[0]
#                             ui.label(f"Variación de precios de {price.symbol}").style('font-weight: bold')
#                             ui.label(f"Variación diaria: {price.day:,.2f} %")
#                             ui.label(f"Variación semanal: {price.week:,.2f} %")
#                             ui.label(f"Variación mensual: {price.month:,.2f} %")
#                             ui.label(f"Variación anual: {price.year:,.2f} %")
                        
#                         else:
#                             ui.label(f"No se encontraron datos para el ticker {ticker}")

#                 with ui.column().style('width: 30%;'):
#                     ui.button('Ver datos de la empresa').on_click(lambda: ui.navigate.to(f'/yfinance/info/{ticker}')).style('width: auto; margin: 0;')

#                 with ui.column().style('width: 30%;'):
#                     with ui.card().style('padding: 20px; border: 1px solid #ccc; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); height: 300px'):
#                         if historical_data:
#                             last_data = historical_data[-1]
#                             previous_data = historical_data[-2] if len(historical_data) > 1 else None

#                             ui.label(f"Datos de la última sesión").style('font-weight: bold')
#                             ui.label(f"Precio apertura de la última sesión: ${last_data.open:,.2f}")
#                             ui.label(f"Precio cierre de la última sesión: ${last_data.close:,.2f}")
#                             ui.label(f"Precio más alto de la última sesión: ${last_data.high:,.2f}")
#                             ui.label(f"Precio más bajo de la última sesión: ${last_data.low:,.2f}")
#                             if previous_data:
#                                 ui.label(f"Precio cierre de la sesión anterior: ${previous_data.close:,.2f}")
#                             else:
#                                 ui.label(f"No se encontró información sobre la sesión anterior.")
#                         else:
#                             ui.label(f"No se encontraron datos históricos para el ticker {ticker}")


from nicegui import ui, Client
from investbook.sources.yfinance.historical import YahooFinanceHistorical
from investbook.sources import AssetsAPI
from investbook.app.front.shared.layout import Layout
from investbook.app.front.shared.colors import Colors
from datetime import datetime, timedelta
from investbook.sources.yfinance.info import YahooFinanceInfo  


class HistoricalData:
    
    def __init__(self) -> None:

        @ui.page('/yfinance/historical/{ticker}')
        def create_stock_card(client: Client, ticker: str, period: str = "1y"):
            
            client.layout.classes(Colors.body)
            Layout()
            
            try:
                # Obtener datos históricos de precios
                yahoo_historical = YahooFinanceHistorical()
                historical_data = yahoo_historical.get_historical_data(ticker, "1y")
                

                # Obtener datos de variación de precio
                api_fmp = AssetsAPI(fmp_api_key='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4')
                price_data = api_fmp.fmp.price.change(ticker)
                balance_data = api_fmp.fmp.finance.income_statement(ticker, period = 'annual')
                
                

               # Obtener información financiera (si es necesario)
                yahoo_info = YahooFinanceInfo()
                info_ticker = yahoo_info.get_info(ticker)
                
                # Extraemos los datos
                company_name = info_ticker.company_name if info_ticker else "N/A"
                price = price_data[0] 



                # Datos históricos de precios (si existen)
                dates = [data.date for data in historical_data] if historical_data else []
                close_prices = [data.close for data in historical_data] if historical_data else []

            except Exception as e:
                print(f"Error: {e}")
                return


            # Crear el card de la acción
            with ui.card().classes('w-full max-w-lg p-6 rounded-xl shadow-lg bg-blue-50'):
                # Encabezado con nombre de la compañía y ticker
                with ui.row().classes('items-center justify-between'):
                    ui.label(company_name).classes('text-4xl font-extrabold text-gray-800')
                    ui.label(f'({ticker})').classes('text-sm font-medium text-gray-500')

                ui.separator().classes('my-4 border-gray-300')

                # Tabs y contenido de los estados financieros
                with ui.tabs().classes('mb-4') as tabs:
                    pl = ui.tab('pl')
                    balance = ui.tab('Balance Financiero')
                    cashflow = ui.tab('Ratios y Métricas Financieras')
                     
                with ui.tab_panels(tabs, value=pl):
                    with ui.tab_panel(pl).classes('bg-blue-50'):
                        with ui.column().classes('gap-2 p-4 rounded-lg shadow-sm'):
                            ui.label(f'Revenue: ${info_ticker.total_revenue:,.2f}').classes('text-base text-gray-700')
                            ui.label(f'Dividends: ${info_ticker.dividend_yield:,.2f}').classes('text-base text-gray-700')
                            ui.label(f'Net Income: ${info_ticker.net_income:,.2f}').classes('text-base text-gray-700')        
                    
                    with ui.tab_panel(balance).classes('bg-blue-50'):
                        if balance_data:
                            balance = sorted(balance_data, key=lambda x: datetime.strptime(x.date, '%Y-%m-%d'), reverse=True)
                            last_financial = balance[:1]
                            for financial in last_financial:
                                with ui.column().classes('gap-2 p-4 rounded-lg shadow-sm'):                       
                                    ui.label(f'Total de Gastos: ${financial.costAndExpenses:,.2f}').classes('text-base text-gray-700')
                                    ui.label(f'Margen de beneficio neto: ${financial.netIncomeRatio * 100:,.2f}').classes('text-base text-gray-700')
                                    ui.label(f'EBITDA: ${financial.ebitda:,.2f}').classes('text-base text-gray-700')

                    with ui.tab_panel(cashflow).classes('bg-blue-50'):
                        with ui.column().classes('gap-2 p-4 rounded-lg shadow-sm'):
                            ui.label(f"Rentabilidad sobre activos: {info_ticker.return_on_assets:,.3f}%").classes('text-base text-gray-700')
                            ui.label(f"Deuda sobre capital: ${info_ticker.debt_to_equity:,.3f}").classes('text-base text-gray-700')
                            ui.label(f"Ratio corriente: {info_ticker.current_ratio:,.3f}").classes('text-base text-gray-700')

                # Datos de cotización estilizados
                with ui.row().classes('items-center justify-center gap-8 mb-4'):
                    for record in historical_data[0:1]: 
                        ui.label(f'${record.open:,.2f}').classes('text-4xl font-extrabold text-gray-800')
                    # color = 'green' if price >= 0 else 'red'
                    # ui.label(f'{price:+.2f}%').classes(f'text-4xl font-extrabold text-{color}-500')

                # Gráfico de líneas con histórico de precios
                if historical_data:
                    linechart = ui.echart({
                        'xAxis': {'type': 'category', 'data': dates},
                        'yAxis': {'type': 'value'},
                        'series': [{
                            'data': close_prices,
                            'type': 'line',
                            'smooth': True,
                            'areaStyle': {'color': 'rgba(0, 112, 243, 0.2)'},
                            'lineStyle': {'color': '#0070F3', 'width': 3}
                        }],
                        'tooltip': {'trigger': 'axis'}
                    }).classes('w-full h-48 rounded-lg shadow-sm')
