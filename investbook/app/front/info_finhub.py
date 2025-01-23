from nicegui import ui, Client
from investbook.sources import AssetsAPI  
from investbook.app.front.shared.layout import Layout
from investbook.app.front.shared.colors import Colors




class Info_finhub:
    
    def __init__(self) -> None:

        @ui.page('/finhub/info/{ticker}')
        async def root(client: Client, ticker: str):

            client.layout.classes(Colors.body)
            Layout()

            info_ticker=None
            info_cuote=None
            info_trends=None
            
            try:
                api=AssetsAPI(finhub_api_key='ct8pt19r01qpc9s002l0ct8pt19r01qpc9s002lg')
                
                info_ticker = api.finhub.get_symbol.company_profile(ticker)  
                
                info_cuote = api.finhub.get_quote.get_cuote(ticker)
                
                info_trends = api.finhub.get_symbol.get_trends(ticker)
                
                
            except Exception as e:
                print(e)
                
            if info_ticker:
                
                price = info_ticker
                ui.label(f"Información básica de la empresa").style('font-weight: bold')
                ui.label(f"Nombre: {price.name}")
                ui.label(f"Símbolo: {price.ticker}")
                ui.label(f"Mercado en el que opera: {price.exchange}")
                ui.label(f"Sector industrial: {price.finnhubIndustry}")
                ui.label(f"Capitalización de mercado: {price.marketCapitalization}")
                ui.label(f"Moneda en la que opera: {price.currency}")
                ui.label(f" ")
                
            if info_cuote:
                
                ui.label(f"Datos de cotización").style('font-weight: bold')
                ui.label(f"Precio apertura de la última sesión: {info_cuote.o}")
                ui.label(f"Precio cierre de la última sesión: {info_cuote.c}")
                ui.label(f"Precio más alto de la última sesión: {info_cuote.h}")
                ui.label(f"Precio más bajo de la última sesión: {info_cuote.l}")
                ui.label(f"Precio cierre de la sesión anterior: {info_cuote.pc}")
                ui.label(f" ")
                
            if info_trends:
                
                trend = info_trends[0]
                ui.label(f"Recomendación de un analista").style('font-weight: bold')
                ui.label(f"Periodo de análisis: {trend.period}")
                ui.label(f"Precio de compra: {trend.buy}")
                ui.label(f"Precio de venta: {trend.sell}")
                ui.label(f"Precio para mantener: {trend.hold}")