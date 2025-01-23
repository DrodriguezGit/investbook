from nicegui import ui
from dataclasses import dataclass
from investbook.app.front.shared.colors import Colors


@dataclass
class NavItem:
    text: str
    rt: str = None  # Hacer que la ruta sea opcional para permitir submenús
    icon: str = None
    subitems: list['NavItem'] = None  # Lista opcional de subelementos

class NavigationMenu(ui.left_drawer):

    classes_def = f'{Colors.nav} w-full px-0 pe-2 py-2 pt-6 shadow-inner'
    width = 280
    breakpoint = 750
    button_classes = f'w-full h-12 text-xl font-bold font-mono rounded-e-full'
    button_props = 'flat align="left"'

    def __init__(self, items: list[NavItem]) -> None:
        super().__init__(value=0)
        self.classes(self.classes_def)
        self.props(f'width={self.width} breakpoint={self.breakpoint}')

        with self:
            for item in items:
                self.add_item(item)

    def add_item(self, item: NavItem):
        if item.subitems:  # Si el elemento tiene submenús
            with ui.expansion(text=item.text).classes('w-full text-lg font-semibold mb-2'):
                if item.icon:
                    ui.icon(item.icon).classes('mr-3')
                for subitem in item.subitems:
                    self.add_item(subitem)  # Añadir subelementos recursivamente
        else:  # Si es un elemento simple
            with ui.button(on_click=lambda rt=item.rt: ui.navigate.to(rt)) \
                .classes(self.button_classes).props(self.button_props):
                if item.icon:
                    ui.icon(item.icon).classes('mr-3')  # Icono opcional
                ui.label(item.text)  # Etiqueta del botón