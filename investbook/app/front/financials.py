from nicegui import ui, Client
from investbook.sources import AssetsAPI  
from investbook.app.front.shared.layout import Layout
from investbook.app.front.shared.colors import Colors
from datetime import datetime


class Financials:
    def __init__(self) -> None:
       

        @ui.page('/fmp/financials/{ticker}')
        async def price_details(client: Client, ticker: str):
            
            client.layout.classes(Colors.body)
            
            Layout()

            try:
                api = AssetsAPI(fmp_api_key='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4')

                price_data = api.fmp.finance.income_statement(ticker, period = 'annual') 

            except Exception as e:
                print(e)

       
            if price_data:
    
                sorted_financials = sorted(price_data, key=lambda x: datetime.strptime(x.date, '%Y-%m-%d'), reverse=True)
                
                # Tomamos los tres últimos estados financieros
                last_three_financials = sorted_financials[:3]

                # Creamos una fila para los tres estados financieros
                with ui.row().style('display: flex; justify-content: space-between; width: 100%; gap: 10px;'):
                    for financial in last_three_financials:
                        with ui.column().style('width: 32%'):
                            with ui.card().style('padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0;'):
                                ui.label(f"Símbolo: {financial.symbol}").style('font-weight: bold')
                                ui.label(f"Año calendario: {financial.calendarYear}")
                                ui.label(f"Ingreso total: ${financial.revenue:,.2f}")
                                ui.label(f"Ingreso neto: ${financial.netIncome:,.2f}")
                                ui.label(f"EBITDA: ${financial.ebitda:,.2f}")
                                ui.label(f"EPS: {financial.eps}")
                                ui.label(f"Margen de ganancia bruto: {financial.grossProfitRatio * 100:.2f}%")
                                ui.label(f"Margen de beneficio neto: {financial.netIncomeRatio * 100:.2f}%")
                                ui.label(f"Total de gastos: ${financial.costAndExpenses:,.2f}")
                                ui.label(f"Gastos de ventas y marketing: ${financial.sellingAndMarketingExpenses:,.2f}")
                                ui.label(f"Fecha de aceptación: {financial.acceptedDate}")
            else:
                ui.label(f"No se encontraron datos para el ticker.")
           
