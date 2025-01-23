from nicegui import ui, app
from investbook.app.front.shared.colors import Colors

class Header(ui.header):

    classes_def = f'{Colors.header} row items-center justify-between px-4 py-2'
    icon_size = 'md'
    button_props = 'flat fab color=white'

    def __init__(self, left_drawer: ui.left_drawer) -> None:
        super().__init__(elevated=True)

        self.classes(self.classes_def)
        self.props('reveal elevated')

        with self:
            
            with ui.button(on_click=lambda: left_drawer.toggle()) \
            .classes('p-0').props(self.button_props):
                ui.icon('menu', size=self.icon_size)

            with ui.row().classes('items-center'):
                ui.label('david').classes('text-lg font-mono')
                with ui.column():

                    with ui.button().classes('p-0').props(self.button_props):
                        ui.icon('account_circle', size=self.icon_size)

                        with ui.menu():
                            ui.menu_item('Mis datos')
                            ui.separator()
                            ui.menu_item('Desconectar')