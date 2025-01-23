from nicegui import ui, Client
from investbook.sources import AssetsAPI
from investbook.app.front.shared.layout import Layout
from investbook.app.front.shared.colors import Colors


class Indices:
    def __init__(self) -> None:
        
        @ui.page('/polygon/indices/{ticker}/{date}')
        async def root(client: Client, ticker: str, date: str):
            client.layout.classes(Colors.body)
            Layout()

            try:
                
                api = AssetsAPI(polygon_api_key='1DWuCVNmdWPBcfL8R9pffQ9UacVGA9lK')

                index_data = api.polygon.indices.get_price(ticker, date) 
                
                # Mostrar los resultados
                if index_data:
                    ui.label(f"Datos del índice: {index_data.symbol}")
                    ui.label(f"Apertura: ${index_data.open}")
                    ui.label(f"Máximo: ${index_data.high}")
                    ui.label(f"Mínimo: ${index_data.low}")
                    ui.label(f"Cierre: ${index_data.close}")
                else:
                    ui.label(f"No se encontraron datos para el índice {ticker} en la fecha {date}.")
            except Exception as e:
                ui.label(f"Error al obtener los datos: {e}")

    
