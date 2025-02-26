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
        
        logo_path = '/home/david/investbook/logo.png'

        # Función para abrir el enlace. Está hecho feo pero las imágenes se comportan diferente
        def open_link():
            ui.navigate.to('https://www.triplealpha.in/es/')
            
        def logout_and_redirect():
            ui.navigate.to('/login')

        with self:
            with ui.row().classes("w-full flex items-center justify-between px-4"):
                
                with ui.column().classes("flex-grow flex justify-start"):
                    ui.image(logo_path).on('click', open_link).classes("max-w-xs")

                with ui.column().classes("flex-grow flex justify-left items-left"):
                    ui.image("investbook2.png").classes("w-72")

                with ui.column().classes('flex-none ml-auto'):
                    with ui.row().classes("flex items-center"):
                        ui.label(self.usuario_actual).classes('text-lg font-mono mr-4')

                        with ui.button().classes('p-0').props(self.button_props):
                            ui.icon('account_circle', size=self.icon_size)

                            with ui.menu():
                                ui.menu_item('Mis datos', on_click=self.mostrar_datos) 
                                ui.separator()
                                ui.menu_item('Desconectar', on_click=logout_and_redirect)

        self.dialog = ui.dialog().classes("bg-transparent")

    def mostrar_datos(self):
        """Muestra el pop-up con los tickers guardados."""
        from investbook.app.front.index import Login   

        login = Login()  
        tickers = login.obtener_tickers(self.usuario_actual) 
        
        with self.dialog:
            self.dialog.clear()
            
            with ui.card().classes("max-w-sm mx-auto p-8 bg-gray-100 border-2 rounded-4xl"):
                ui.label(f"Tickers buscados").classes('text-xl font-semibold')
                
                if tickers:
                    for ticker in tickers:
                        ui.label(ticker).classes('text-lg text-gray-700')
                else:
                    ui.label("No tienes tickers guardados").classes('text-lg text-gray-700')
                
                ui.button('Cerrar', on_click=self.dialog.close).classes('mt-4 bg-blue-500 text-white rounded-lg')

        
        self.dialog.open()
