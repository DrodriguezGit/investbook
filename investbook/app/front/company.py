from nicegui import ui, Client
from investbook.sources import AssetsAPI  
from investbook.app.front.shared.layout import Layout
from investbook.app.front.shared.colors import Colors



class Company:
    def __init__(self) -> None:
        
        @ui.page('/fmp/company/{ticker}')
        async def company_details(client: Client, ticker: str):
            
            client.layout.classes(Colors.body)
            
            Layout()

            try:
                
                api = AssetsAPI(fmp_api_key='UhcusRqvRQlT1DkVdH4JFFdW8KRtXEj4')

                price_data = api.fmp.company.get_profile(ticker)  

            except Exception as e:
                
                 ui.label(f"Error al obtener datos de precios: {e}")


            selected_price = next((stock for stock in price_data if stock.symbol == ticker), None)


            if selected_price:
                
                for profile in price_data:

                    ui.label(f"Nombre de la compañía: {profile.companyName}")
                    ui.label(f"Símbolo: {profile.symbol}")
                    ui.label(f"Sector: {profile.sector}")
                    ui.label(f"Industria: {profile.industry}")
                    ui.label(f"Descripción: {profile.description}")
                    ui.label(f"Dirección: {profile.address}")
                    ui.label(f"Ciudad: {profile.city}")
                    ui.label(f"País: {profile.country}")
                    ui.label(f"CEO: {profile.ceo}")
                    ui.label(f"Capitalización de mercado: ${profile.mktCap:,}")
                    ui.label(f"Número promedio de empleados: {profile.fullTimeEmployees}")
                    ui.label(f"Precio actual: ${profile.price}")
                    ui.label(f"Beta: {profile.beta}")
                    ui.label(f"Teléfono: {profile.phone}")
                    ui.label(f"Sitio web: {profile.website}")
                    
            else:
                
                ui.label(f"No se encontraron datos para el ticker {ticker}")       
           
