from nicegui import ui, Client
from investbook.sources import AssetsAPI  
from investbook.sources.yfinance.info import YahooFinanceInfo  
from investbook.app.front.shared.layout import Layout
from investbook.app.front.shared.colors import Colors




class Info:
    
    def __init__(self) -> None:

        @ui.page('/info/{ticker}')
        async def root(client: Client, ticker: str):

            client.layout.classes(Colors.body)
            Layout()

            info_ticker=None
            info_cuote=None
            info_trends=None
            
            try:
                api_fin=AssetsAPI(finhub_api_key='ct8pt19r01qpc9s002l0ct8pt19r01qpc9s002lg')
                
                info_ticker = api_fin.finhub.get_symbol.company_profile(ticker)  
                
                api_fmp = AssetsAPI(fmp_api_key='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4')
                price_data = api_fmp.fmp.price.change(ticker)  
                
               
                yahoo_info = YahooFinanceInfo()
                info_ticker = yahoo_info.get_info(ticker)
                
            except Exception as e:
                print(e)
                
            with ui.row().classes('w-full mt-6'):
                with ui.column().classes('w-full'):
                    with ui.tabs().classes('mb-4 w-full') as tabs:
                        # Definir las pestañas
                        pl = ui.tab('Información básica')  
                        bl = ui.tab('Precio')  
                        cf = ui.tab('Datos financieros')  
            
            with ui.tab_panels(tabs, value=pl):
    
                    # Panel de Información general
                    with ui.tab_panel(pl).classes('bg-blue-50 p-4 rounded-lg shadow-lg'):
                        with ui.column().classes('gap-4'):
                            selected_price = next((stock for stock in price_data if stock.symbol == ticker), None)

                            if selected_price:
                                
                                for profile in price_data:
                                    
                                    ui.label(f"Nombre: {info_ticker.company_name}").classes('text-xl text-blue-800 font-semibold')
                                    ui.label(f"Símbolo: {info_ticker.symbol}").classes('text-lg text-gray-700')
                                    ui.label(f"Sector industrial: {info_ticker.sector}").classes('text-lg text-gray-700')
                                    ui.label(f"Industria: {info_ticker.industry}").classes('text-lg text-gray-700')
                                    ui.label(f"País: {info_ticker.country}").classes('text-lg text-gray-700')
                                    ui.label(f"Empleados a tiempo completo: {info_ticker.full_time_employees}").classes('text-lg text-gray-700')
                                    ui.label(f"Sitio web: {info_ticker.website}").classes('text-lg text-blue-500 underline')

                                    # Información de profile
                                    # ui.label(f"Nombre de la compañía: {profile.companyName}").classes('text-xl text-blue-800 font-semibold')
                                    ui.label(f"Símbolo: {profile.symbol}").classes('text-lg text-gray-700')
                                    ui.label(f"Sector: {profile.sector}").classes('text-lg text-gray-700')
                                    ui.label(f"Industria: {profile.industry}").classes('text-lg text-gray-700')
                                    ui.label(f"Descripción: {profile.description}").classes('text-lg text-gray-700')
                                    ui.label(f"Dirección: {profile.address}").classes('text-lg text-gray-700')
                                    ui.label(f"Ciudad: {profile.city}").classes('text-lg text-gray-700')
                                    ui.label(f"País: {profile.country}").classes('text-lg text-gray-700')
                                    ui.label(f"CEO: {profile.ceo}").classes('text-lg text-gray-700')
                                    ui.label(f"Capitalización de mercado: ${profile.mktCap:,}").classes('text-lg text-gray-700')
                                    ui.label(f"Número promedio de empleados: {profile.fullTimeEmployees}").classes('text-lg text-gray-700')
                                    ui.label(f"Precio actual: ${profile.price}").classes('text-lg text-gray-700')
                                    ui.label(f"Beta: {profile.beta}").classes('text-lg text-gray-700')
                                    ui.label(f"Teléfono: {profile.phone}").classes('text-lg text-gray-700')
                                    ui.label(f"Sitio web: {profile.website}").classes('text-lg text-blue-500 underline')
                

 