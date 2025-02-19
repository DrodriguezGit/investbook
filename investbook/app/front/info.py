from nicegui import ui, Client
from investbook.sources import AssetsAPI  
from investbook.sources.yfinance.info import YahooFinanceInfo  
from investbook.app.front.shared.colors import Colors
from datetime import datetime
from investbook.sources.yfinance.info import YahooFinanceInfo  
from investbook.sources.yfinance.historical import YahooFinanceHistorical




class Info:
    
    def __init__(self) -> None:

        @ui.page('/info/{ticker}')
        async def root(client: Client, ticker: str):

            client.layout.classes(Colors.body)
            # Layout()

            info_ticker=None

            try:
                api = AssetsAPI(fmp_api_key='qd8qbTjUzah8tDi3mwM1MaDeskOanjwy')
                yahoo_info = YahooFinanceInfo()
                yahoo_historical = YahooFinanceHistorical()
                
                info_ticker = yahoo_info.get_info(ticker) 
                historical_data = yahoo_historical.get_historical_data(ticker, "1y")                    
                dates = [data.date for data in historical_data] if historical_data else []
                close_prices = [data.close for data in historical_data] if historical_data else []
                
                price_data = api.fmp.finance.income_statement(ticker, period = 'annual')    
                
                
            except Exception as e:
                print(f"Error: {e}")
        
            
        
            ui.button('Volver', on_click=lambda:  ui.navigate.to(f"/")).style('margin-left: 20px')
            ui.label(f" ")
            
            if info_ticker:
                
                
                ui.label(f"Información básica de la empresa").style('font-weight: bold; font-size: 18px; margin-bottom: 20px; margin-left: 20px')

                
                with ui.row().style('display: flex; justify-content: space-between; width: 100%; gap: 20px;'):
                    with ui.column().style('display: flex; justify-content: space-between width: 23%; margin-left: 20px'):
                        ui.label("Datos Generales").classes('text-lg font-semibold text-center mb-4')
                        with ui.card().style('padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); height: 350px;'):
                            ui.label(f"Nombre: {info_ticker.company_name}").classes('text-base text-gray-700')
                            ui.label(f"Símbolo: {info_ticker.symbol}").classes('text-base text-gray-700')
                            ui.label(f"Sector industrial: {info_ticker.sector}").classes('text-base text-gray-700')
                            ui.label(f"Industria: {info_ticker.industry}").classes('text-base text-gray-700')
                            ui.label(f"País: {info_ticker.country}").classes('text-base text-gray-700')

                    # Columna de Finanzas y Rendimiento
                    with ui.column().style('display: flex; justify-content: space-between width: 23%; margin-left: 10px'):
                        ui.label("Finanzas y Rendimiento").classes('text-lg font-semibold text-center mb-4')
                        with ui.card().style('padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); height: 350px;'):
                            ui.label(f"Capitalización de mercado: ${info_ticker.market_cap:,.2f}").classes('text-base text-gray-700')
                            ui.label(f"Precio actual: ${info_ticker.current_price:,.2f}").classes('text-base text-gray-700')
                            ui.label(f"Cierre anterior: ${info_ticker.previous_close:,.2f}").classes('text-base text-gray-700')
                            ui.label(f"Ingresos totales: ${info_ticker.total_revenue:,.2f}").classes('text-base text-gray-700')
                            ui.label(f"Ingreso neto: ${info_ticker.net_income:,.2f}").classes('text-base text-gray-700')
                            ui.label(f"Flujo de caja libre: ${info_ticker.free_cashflow:,.2f}").classes('text-base text-gray-700')
                     

                    # Columna de Ratios y Métricas Financieras
                    with ui.column().style('display: flex; justify-content: space-between width: 23%; margin-left: 10px'):
                        ui.label("Ratios y Métricas Financieras").classes('text-lg font-semibold text-center mb-4')
                        with ui.card().style('padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); height: 350px;'):
                            sorted_financials = sorted(price_data, key=lambda x: datetime.strptime(x.date, '%Y-%m-%d'), reverse=True)
                            last_three_financials = sorted_financials[:1]  # Tomamos el último estado financiero
                            for financial in last_three_financials:
                                ui.label(f"Rentabilidad sobre activos: {info_ticker.return_on_assets:,.3f}%").classes('text-base text-gray-700')
                                ui.label(f"Rentabilidad sobre el capital: {info_ticker.return_on_equity:,.3f}%").classes('text-base text-gray-700')
                                ui.label(f"Deuda sobre capital: {info_ticker.debt_to_equity:,.3f}").classes('text-base text-gray-700')
                                ui.label(f"Ratio rápido: {info_ticker.quick_ratio:,.3f}").classes('text-base text-gray-700')
                                ui.label(f"Ratio corriente: {info_ticker.current_ratio:,.3f}").classes('text-base text-gray-700')
                                ui.label(f"EBITDA: ${financial.ebitda:,.2f}").classes('text-base text-gray-700')
                                ui.label(f"EPS: {financial.eps}").classes('text-base text-gray-700')
                                

                    # Columna de Información Adicional
                    with ui.column().style('display: flex; justify-content: space-between; width: 23%; margin-left: 10px'):
                        ui.label("Información Adicional").classes('text-lg font-semibold text-center mb-4')
                        with ui.card().style('padding: 20px; border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); height: 350px;'):
                            ui.label(f"Empleados a tiempo completo: {info_ticker.full_time_employees}").classes('text-base text-gray-700')
                            ui.label(f"Sitio web: {info_ticker.website}").classes('text-base text-blue-500 underline')
                
                
                
                with ui.row().style('display: flex; justify-content: space-between; width: 100%; gap: 20px; margin-top: 20px;'):
                    # Columna con la etiqueta "Cuenta de resultados"
                    with ui.column().style('width: 23%; margin-left: 10px'):
                        sorted_financials = sorted(price_data, key=lambda x: datetime.strptime(x.date, '%Y-%m-%d'), reverse=True)
                        last_three_financials = sorted_financials[:1]  # Tomamos el último estado financiero
                        for financial in last_three_financials:
                            if price_data:
                                ui.label("Cuenta de resultados").classes('text-lg font-semibold text-center mb-4').style('margin-left: 10px')
                                with ui.card().style('margin-left: 10px; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);'):
                                    ui.label(f"Símbolo: {financial.symbol}").classes('font-semibold')
                                    ui.label(f"Año calendario: {financial.calendarYear}")
                                    ui.label(f"Ingreso total: ${financial.revenue:,.2f}")
                                    ui.label(f"Ingreso neto: ${financial.netIncome:,.2f}")
                                    ui.label(f"Margen de ganancia bruto: {financial.grossProfitRatio * 100:.2f}%")
                                    ui.label(f"Margen de beneficio neto: {financial.netIncomeRatio * 100:.2f}%")
                                    ui.label(f"Total de gastos: ${financial.costAndExpenses:,.2f}")
                                    ui.label(f"Gastos de ventas y marketing: ${financial.sellingAndMarketingExpenses:,.2f}")
                            else:
                                ui.label("No se encontraron datos para el ticker.").classes('text-lg text-red-500 font-semibold')

                    # Columna con el gráfico de resultados
                    with ui.column().style('width: 70%; height: 70%;  margin-right: 95px'):
                        ui.label(f"Gráfico anual de {info_ticker.company_name}").classes('text-lg font-semibold text-center mb-4').style('margin-left: 10px')
                        with ui.card().style('width: 100%; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);'):
                            if historical_data:
                                formatted_close_prices = [f"{price:.2f}" for price in close_prices]
                                linechart = ui.echart({
                                    'xAxis': {'type': 'category', 'data': dates},
                                    'yAxis': {'type': 'value'},
                                    'series': [{
                                        'data': formatted_close_prices,
                                        'type': 'line',
                                        'smooth': True,
                                        'areaStyle': {'color': 'rgba(0, 112, 243, 0.2)'},
                                        'lineStyle': {'color': '#0070F3', 'width': 3}
                                    }],
                                    'tooltip': {'trigger': 'axis'}
                                }).style('width: 100%; height: 280px;')  # Ajusta la altura aquí según lo necesites


                 