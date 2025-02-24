from nicegui import ui
from investbook.app.front.shared.colors import Colors

class Header(ui.header):

    classes_def = f'{Colors.header} row items-center justify-end px-4 py-2'
    icon_size = 'md'
    button_props = 'flat fab color=white'

    def __init__(self, usuario_actual) -> None:
        super().__init__(elevated=True)

        self.usuario_actual = usuario_actual  
        self.classes(self.classes_def)
        self.props('reveal elevated')

        with self:
            with ui.row().classes('items-center justify-end '):
                ui.label(self.usuario_actual).classes('text-lg font-mono')

                with ui.column():
                    with ui.button().classes('p-0').props(self.button_props):
                        ui.icon('account_circle', size=self.icon_size)

                        with ui.menu():
                            ui.menu_item('Mis datos', on_click=self.mostrar_datos) 
                            ui.separator()
                            ui.menu_item('Desconectar')

    def mostrar_datos(self):
        """Muestra el pop-up con los tickers guardados."""
        from investbook.app.front.index import Login  # 

        login = Login()  
        tickers = login.obtener_tickers(self.usuario_actual) 
        
        with ui.dialog() as dialog:
            with ui.card().classes("border-2 rounded-4xl bg-gray-100 p-8 w-96"):
                ui.label(f"Tickers buscados").classes('text-xl font-semibold')
                
                if tickers:
                    for ticker in tickers:
                        ui.label(ticker).classes('text-lg text-gray-700')
                else:
                    ui.label("No tienes tickers guardados").classes('text-lg text-gray-700')
                
                ui.button('Cerrar', on_click=dialog.close).classes('mt-4 bg-blue-500 text-white rounded-lg')
        
        dialog.open()
