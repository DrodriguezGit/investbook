from nicegui import ui
from investbook.app.front.shared.colors import Colors

class Header(ui.header):

    classes_def = f'{Colors.header} row items-center justify-end px-4 py-2'
    icon_size = 'md'
    button_props = 'flat fab color=white'

    def __init__(self) -> None:
        super().__init__(elevated=True)

        self.classes(self.classes_def)
        self.props('reveal elevated')

        with self:
            # Eliminamos la parte de left_drawer, y solo ponemos el botón de menú
            with ui.row().classes('items-center justify-end '):
                ui.label('david').classes('text-lg font-mono')

                # Ahora solo el botón de perfil
                with ui.column():
                    with ui.button().classes('p-0').props(self.button_props):
                        ui.icon('account_circle', size=self.icon_size)

                        with ui.menu():
                            ui.menu_item('Mis datos')
                            ui.separator()
                            ui.menu_item('Desconectar')
