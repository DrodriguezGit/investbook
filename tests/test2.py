from nicegui import ui
from nicegui.binding import BindableProperty
import random
from datetime import datetime, timedelta
 
# Función para generar datos históricos
def generate_historical_data(days):
    return [random.uniform(100, 150) for _ in range(days)]
 
# Datos ficticios iniciales
historical_prices = generate_historical_data(365 * 5)  # 5 años de datos


class Selection:
    selected_range: str = BindableProperty()
    
    def __init__(self):
        self.selected_range=None       
        
selection=Selection()
 
def update_chart():
    """Actualiza el gráfico según el rango temporal seleccionado."""
    now = datetime.now()
    if selection.selected_range == '1M':
        days = 30
    elif selection.selected_range == '3M':
        days = 90
    elif selection.selected_range == '6M':
        days = 180
    elif selection.selected_range == '1A':
        days = 365
    elif selection.selected_range == 'YTD':
        start_of_year = datetime(now.year, 1, 1)
        days = (now - start_of_year).days
    elif selection.selected_range == '5A':
        days = 365 * 5
    else:
        days = 365  # Fallback
 
    dates = [(now - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(days)][::-1]
    prices = historical_prices[-days:]
 
    line_chart.options['xAxis']['data'] = dates
    line_chart.options['series'][0]['data'] = prices
    line_chart.update()
 
with ui.card().classes('w-full max-w-lg p-6 rounded-xl shadow-lg bg-gradient-to-br from-blue-50 to-blue-100'):
    # Encabezado
    with ui.row().classes('items-center justify-between mb-4'):
        ui.label('TechCorp').classes('text-2xl font-extrabold text-gray-800')
        ui.label('(TC)').classes('text-sm font-medium text-gray-500')
    ui.separator().classes('my-4 border-gray-300')
 
    # Botones de filtro temporal
    with ui.row().classes('items-center justify-center gap-4 mb-4'):
        for label in ['1M', '3M', '6M', '1A', 'YTD', '5A']:
            ui.button(label, on_click=lambda: update_chart) \
                .classes('px-4 py-2 rounded-full text-sm font-semibold bg-white shadow-md hover:bg-blue-100').bind_text_to(selection, 'selected_range')
 
    # Gráfico de líneas
    dates = [(datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(365)][::-1]
    line_chart = ui.echart({
        'xAxis': {'type': 'category', 'data': dates},
        'yAxis': {'type': 'value'},
        'series': [{
            'data': historical_prices[-365:],
            'type': 'line',
            'smooth': True,
            'areaStyle': {'color': 'rgba(0, 112, 243, 0.2)'},
            'lineStyle': {'color': '#0070F3', 'width': 3}
        }],
        'tooltip': {'trigger': 'axis'}
    }).classes('w-full h-48 rounded-lg shadow-sm')
 
# Observador para actualizar el gráfico al cambiar el rango seleccionado 
ui.run()