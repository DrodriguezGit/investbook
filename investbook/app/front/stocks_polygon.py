from nicegui import ui, Client
from investbook.sources import AssetsAPI
from investbook.app.front.shared.layout import Layout
from investbook.app.front.shared.colors import Colors

class Stocks_pol:
    def __init__(self) -> None:
        
        @ui.page('/polygon/stocks/{ticker}/{date}')
        async def root(client: Client, ticker: str, date: str):
            client.layout.classes(Colors.body)
            Layout()

            try:
                api = AssetsAPI(polygon_api_key='1DWuCVNmdWPBcfL8R9pffQ9UacVGA9lK')
                data = api.polygon.stocks.get_price(ticker, date)  

                if data:

                    with ui.card().style('padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0; width: 100%; max-width: 300px; margin-left: 0; margin-right: 0; margin-top: 20px;'):
                        
                        ui.label(f"Datos del índice: {data.symbol}").style('font-weight: bold; font-size: 18px; margin-bottom: 10px;')

                        with ui.column().style('padding-left: 20px;'):
                            ui.label(f"• Fecha: {data.date}")
                            ui.label(f"• Apertura: ${data.open}")
                            ui.label(f"• Máximo: ${data.high}")
                            ui.label(f"• Mínimo: ${data.low}")
                            ui.label(f"• Cierre: ${data.close}")
                            ui.label(f"• Volumen: {data.volume}")
                            ui.label(f"• After Hours: ${data.afterHours}")
                            ui.label(f"• Pre-Market: ${data.preMarket}")

                else:
                    ui.label(f"No se encontraron datos para el índice {ticker} en la fecha {date}.")
                    
            except Exception as e:
                ui.label(f"Error al obtener los datos: {e}")
