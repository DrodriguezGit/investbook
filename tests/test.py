from nicegui import ui
from investbook.app.front.shared.layout import Layout
from investbook.app.front.shared.colors import Colors
import yfinance as yf

def get_yfinance_data(ticker: str, period: str = "1y"):
    # Usamos la librería yfinance para obtener los datos
    stock = yf.Ticker(ticker)
    history = stock.history(period=period)
    company_name = stock.info['shortName']
    price = stock.history(period="1d")['Close'][0]
    dates = history.index.strftime('%Y-%m-%d').tolist()
    close_prices = history['Close'].tolist()
    
    # Datos adicionales de la compañía
    total_revenue = stock.info.get('totalRevenue', 'N/A')
    dividend_yield = stock.info.get('dividendYield', 'N/A')
    net_income = stock.info.get('netIncomeToCommon', 'N/A')
    cost_and_expenses = stock.info.get('totalCashFromOperatingActivities', 'N/A')
    net_income_ratio = stock.info.get('netProfitMargin', 'N/A')
    ebitda = stock.info.get('ebitda', 'N/A')
    return_on_assets = stock.info.get('returnOnAssets', 'N/A')
    debt_to_equity = stock.info.get('debtToEquity', 'N/A')
    current_ratio = stock.info.get('currentRatio', 'N/A')
    
    return {
        'company_name': company_name,
        'price': price,
        'dates': dates,
        'close_prices': close_prices,
        'total_revenue': total_revenue,
        'dividend_yield': dividend_yield,
        'net_income': net_income,
        'cost_and_expenses': cost_and_expenses,
        'net_income_ratio': net_income_ratio,
        'ebitda': ebitda,
        'return_on_assets': return_on_assets,
        'debt_to_equity': debt_to_equity,
        'current_ratio': current_ratio
    }

def create_stock_card(ui, ticker: str, period: str = "1y"):
    data = get_yfinance_data(ticker, period)  # Obtener los datos del ticker
    
    # Configuración de la tarjeta
    with ui.card().classes('w-full p-6 rounded-xl shadow-lg bg-blue-50'):
        with ui.column().classes('h-24'):
            ui.label(data['company_name']).classes('text-4xl font-extrabold text-gray-800 text-center')
            ui.label(f'({ticker})').classes('text-sm font-medium text-gray-500').style('align-self: flex-start')

        ui.separator().classes('my-4 border-gray-300')

        # Pestañas
        with ui.column().classes('w-full') as container:
            with ui.tabs().classes('mb-4 w-full').style('border-bottom: 2px solid #e2e8f0 padding-left: 20px; padding-right: 20px') as tabs:
                pl = ui.tab('Bº')
                bl = ui.tab('BF')
                cf = ui.tab('RyMF')

            with ui.tab_panels(tabs, value=pl):
                with ui.tab_panel(pl).classes('bg-blue-50'):
                    with ui.column().classes('gap-2 p-4 rounded-lg shadow-sm'):
                        ui.label(f'Revenue: ${data["total_revenue"]:,.2f}').classes('text-base text-gray-700')
                        ui.label(f'Dividends: ${data["dividend_yield"]:,.2f}').classes('text-base text-gray-700')
                        ui.label(f'Net Income: ${data["net_income"]:,.2f}').classes('text-base text-gray-700')

                with ui.tab_panel(bl).classes('bg-blue-50'):
                    with ui.column().classes('gap-2 p-4 rounded-lg shadow-sm'):
                        ui.label(f'Total de Gastos: ${data["cost_and_expenses"]:,.2f}').classes('text-base text-gray-700')
                        ui.label(f'Margen de beneficio neto: {data["net_income_ratio"] * 100:,.2f}%').classes('text-base text-gray-700')
                        ui.label(f'EBITDA: ${data["ebitda"]:,.2f}').classes('text-base text-gray-700')

                with ui.tab_panel(cf).classes('bg-blue-50'):
                    with ui.column().classes('gap-2 p-4 rounded-lg shadow-sm'):
                        ui.label(f"Rentabilidad sobre activos: {data['return_on_assets'] * 100:,.2f}%").classes('text-base text-gray-700')
                        ui.label(f"Deuda sobre capital: {data['debt_to_equity']:,.3f}").classes('text-base text-gray-700')
                        ui.label(f"Ratio corriente: {data['current_ratio']:,.3f}").classes('text-base text-gray-700')

        with ui.row().classes('items-center justify-center gap-8 mb-4'):
            ui.label(f'${data["price"]:,.2f}').classes('text-4xl font-extrabold text-gray-800')

        # Gráfico
        linechart = ui.echart({
            'xAxis': {'type': 'category', 'data': data['dates'][::-1], 'axisLabel': {'fontSize': 10}},
            'yAxis': {'type': 'value'},
            'series': [{
                'data': data['close_prices'][::-1],
                'type': 'line',
                'smooth': True,
                'areaStyle': {'color': 'rgba(0, 112, 243, 0.2)'},
                'lineStyle': {'color': '#0070F3', 'width': 3}
            }],
            'tooltip': {'trigger': 'axis'}
        }).classes('w-full h-48 rounded-lg shadow-sm')


# Configuración de la página principal
@ui.page('/')
def main():
    tickers = ['IDEXY', 'NVIDIA', 'AMZN', 'NEO', 'GOOGL', 'META']  
    ui.layout.classes('bg-gray-100')  # Establece un fondo de página

    # Fila 1
    with ui.row().classes('flex gap-8 justify-center'):
        for i in range(3):  
            with ui.column().classes('w-full max-w-sm p-4'):
                create_stock_card(ui, tickers[i])

    with ui.row().classes('flex gap-8 justify-center mt-8'):
        for i in range(3, 6):  
            with ui.column().classes('w-full max-w-sm p-4'):
                create_stock_card(ui, tickers[i])

# Iniciar la aplicación
ui.run()
