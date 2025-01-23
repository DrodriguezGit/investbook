from __future__ import annotations
from nicegui import ui
from dataclasses import dataclass
from investbook.app.front.shared.colors import Colors

@dataclass
class BaseCardItem:
    icon: str
    text: str

@dataclass
class BaseCardElement:
    id: str
    description: str


class BaseCard(ui.card):

    main_color = 'blue'

    card_classes = f'm-4 w-80 h-auto p-6 shadow-2xl rounded-3xl bg-gradient-to-b from-{main_color}-500 via-{main_color}-400 to-{main_color}-400 text-white'
    title_classes = 'text-2xl font-extrabold font-mono'
    delete_button_props = 'flat fab-mini'
    navigation_button_classes = 'hover:scale-105'
    navigation_button_props = 'outline rounded color=white'
    items_classes = 'items-center space-x-3'
    label_classes = 'text-lg font-medium'
    icon_size = 'md'
     
    def __init__(
            self,
            title: str,
            main_card_element: BaseCardElement,
            card_items: list[BaseCardItem]
        ) -> None:

        super().__init__()

        self.title = title

        self.id_estudio = main_card_element.id

        self.classes(self.card_classes)

        with self:
            # Título de la card
            with ui.row().classes('w-full justify-between items-center'):
                ui.label(f'{title}').classes(self.title_classes)

                with ui.button().classes('hover:scale-105').props(self.delete_button_props):
                    ui.icon('delete', color='white', size='sm')
                    with ui.menu():
                        self.borrar_item = ui.menu_item(f'Borrar {main_card_element.description}').classes('bg-red-400 text-white')
            
            # Elementos con iconos en el cuerpo de la card
            ui.separator().classes('bg-white')
            with ui.column().classes('space-y-4 mb-6'):
                for item in card_items:
                    with ui.row().classes(self.items_classes):
                        ui.icon(item.icon, size=self.icon_size, color=Colors.icon)
                        ui.label(item.text).classes(self.label_classes)
