from nicegui import ui, Client
from investbook.sources import AssetsAPI  
from investbook.app.front.shared.layout import Layout
from investbook.app.front.shared.colors import Colors
from datetime import datetime



class Dividends:
    
    def __init__(self) -> None:
        
        @ui.page('/fmp/dividends/{ticker}')
        async def fmp_dividends(client: Client, ticker: str):
            
            client.layout.classes(Colors.body)
            Layout()  

            try:
                api = AssetsAPI(fmp_api_key='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4')
                dividend_data = api.fmp.dividends.historical(ticker)  

            except Exception as e:
                 ui.label(f"Error al obtener datos de precios: {e}")

       
            if dividend_data:
                # Ordenamos los dividendos por fecha (más recientes primero)
                sorted_dividends = sorted(dividend_data, key=lambda x: datetime.strptime(x.date, '%Y-%m-%d'), reverse=True)
                
                # Tomamos los tres últimos dividendos
                last_three_dividends = sorted_dividends[:3]

                # Creamos una fila para los tres dividendos
                with ui.row().style('display: flex; justify-content: space-between; width: 100%; gap: 10px;'):
                    for dividend in last_three_dividends:
                        with ui.column().style('width: 32%'):
                            with ui.card().style('padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0;'):
                                ui.label(f"Fecha del dividendo: {dividend.date}").style('font-weight: bold')
                                ui.label(f"Etiqueta: {dividend.label}")
                                ui.label(f"Dividendo ajustado: ${dividend.adjDividend:,.2f}")
                                ui.label(f"Dividendo: ${dividend.dividend:,.2f}")
                                ui.label(f"Fecha de registro: {dividend.recordDate}")
                                ui.label(f"Fecha de pago: {dividend.paymentDate}")
                                ui.label(f"Fecha de declaración: {dividend.declarationDate}")
            else:
                ui.label(f"No se encontraron datos para el ticker.")
           
