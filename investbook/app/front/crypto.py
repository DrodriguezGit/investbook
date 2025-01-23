from nicegui import ui, Client
from investbook.sources import AssetsAPI
from investbook.app.front.shared.layout import Layout
from investbook.app.front.shared.colors import Colors

class Crypto:
    def __init__(self) -> None:
        
        @ui.page('/polygon/cryptos/{crypto}/{currency}/{date}')
        async def root(client: Client, crypto: str, currency: str, date: str):
            client.layout.classes(Colors.body)
            Layout()

            try:
                api = AssetsAPI(polygon_api_key='1DWuCVNmdWPBcfL8R9pffQ9UacVGA9lK')
                crypto_data = api.polygon.cryptos.get_price(crypto, currency, date)  
                
                if crypto_data:
                    ui.label(f"Datos de la criptomoneda: {crypto_data.symbol}")
                    ui.label(f"Fecha: {crypto_data.day[:10]}")  # Muestra solo la fecha (YYYY-MM-DD)
                    ui.label(f"Apertura: ${crypto_data.open}")
                    ui.label(f"Cierre: ${crypto_data.close}")
                else:
                    ui.label(f"No se encontraron datos para {crypto} en la fecha {date} y divisa {currency}.")
            except Exception as e:
                ui.label(f"Error al obtener los datos: {e}")
