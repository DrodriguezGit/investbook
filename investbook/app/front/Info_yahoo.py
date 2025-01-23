from nicegui import ui, Client
from investbook.sources.yfinance.info import YahooFinanceInfo  
from investbook.app.front.shared.layout import Layout
from investbook.app.front.shared.colors import Colors


class Info_yahoo:
    
    def __init__(self) -> None:

        @ui.page('/yfinance/info/{ticker}')
        async def root(client: Client, ticker: str):

            client.layout.classes(Colors.body)
            Layout()

            try:
                yahoo_info = YahooFinanceInfo()
                info_ticker = yahoo_info.get_info(ticker)

            except Exception as e:
                print(f"Error: {e}")
            
            if info_ticker:
                
                ui.label(f"Información básica de la empresa").style('font-weight: bold; font-size: 18px; margin-bottom: 20px; margin-left: 30px')

                
                with ui.row().style('display: flex; justify-content: space-between; width: 100%; gap: 10px;'):

                    
                    with ui.column().style('width: 24%; margin-left: 30px'):
                        ui.label("Datos Generales").style('font-weight: bold; margin-bottom: 10px; text-align: center')
                        with ui.card().style('padding: 20px; border: 1px solid #ccc; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); height: 350px;'):
                            ui.label(f"Nombre: {info_ticker.company_name}")
                            ui.label(f"Símbolo: {info_ticker.symbol}")
                            ui.label(f"Sector industrial: {info_ticker.sector}")
                            ui.label(f"Industria: {info_ticker.industry}")
                            ui.label(f"País: {info_ticker.country}")

                   
                    with ui.column().style('width: 24%; margin-left: -10%'):
                        ui.label("Finanzas y Rendimiento").style('font-weight: bold; margin-bottom: 10px; text-align: center')
                        with ui.card().style('padding: 20px; border: 1px solid #ccc; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); height: 350px;'):
                            ui.label(f"Capitalización de mercado: ${info_ticker.market_cap:,.2f}")
                            ui.label(f"Precio actual: ${info_ticker.current_price:,.2f}")
                            ui.label(f"Cierre anterior: ${info_ticker.previous_close:,.2f}")
                            ui.label(f"Dividendos: {info_ticker.dividend_yield}%")
                            ui.label(f"Ingresos totales: ${info_ticker.total_revenue:,.2f}")
                            ui.label(f"Ingreso neto: ${info_ticker.net_income:,.2f}")
                            ui.label(f"Flujo de caja libre: ${info_ticker.free_cashflow:,.2f}")

                    
                    with ui.column().style('width: 24%; margin-left: -10%'):
                        ui.label("Ratios y Métricas Financieras").style('font-weight: bold; margin-bottom: 10px; text-align: center')
                        with ui.card().style('padding: 20px; border: 1px solid #ccc; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); height: 350px;'):
                            ui.label(f"Rentabilidad sobre activos: {info_ticker.return_on_assets:,.3f}%")
                            ui.label(f"Rentabilidad sobre el capital: {info_ticker.return_on_equity:,.3f}%")
                            ui.label(f"Deuda sobre capital: {info_ticker.debt_to_equity:,.3f}")
                            ui.label(f"Ratio rápido: {info_ticker.quick_ratio:,.3f}")
                            ui.label(f"Ratio corriente: {info_ticker.current_ratio:,.3f}")
                            ui.label(f"Recomendación: {info_ticker.recommendation}")

                    
                    with ui.column().style('width: 24%; margin-left: -10%'):
                        ui.label("Información Adicional").style('font-weight: bold; margin-bottom: 10px; text-align: center')
                        with ui.card().style('padding: 20px; border: 1px solid #ccc; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); height: 350px;'):
                            ui.label(f"Empleados a tiempo completo: {info_ticker.full_time_employees}")
                            ui.label(f"Sitio web: {info_ticker.website}")
                    
                    
                ui.label(f"Otras herramientas").style('font-weight: bold; font-size: 18px; margin-bottom: 20px; margin-top: 40px; margin-left: 30px')

                
                with ui.row().style('display: flex; justify-content: space-between; width: 100%; margin-left: 30px'):  
                    with ui.column().style('width: 24%'):
                        ui.button('Últimas Cuentas de Resultados').on_click(lambda: ui.navigate.to(f'/fmp/financials/{ticker}')).style('width: auto; margin: 0;')

                    with ui.column().style('width: 24%'):
                        ui.button('Ver dividendos').on_click(lambda: ui.navigate.to(f'/fmp/dividends/{ticker}')).style('width: auto; margin: 0;')
                        
                    with ui.column().style('width: 24%'):
                        ui.button('Ver el gráfico').on_click(lambda: ui.navigate.to(f'/yfinance/historical/{ticker}')).style('width: auto; margin: 0;')

                    with ui.column().style('width: 24%'):
                        ui.button('Ver en una fecha específica').on_click(lambda: ui.navigate.to(f'/polygon/stocks')).style('width: auto; margin: 0;')

            else:
                ui.label("No se pudo obtener la información del ticker.")
                