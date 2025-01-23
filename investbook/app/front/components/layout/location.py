from __future__ import annotations
from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from dataclasses import dataclass

@dataclass
class LocationItem:
    navigate_to: str = None
    label: str = None

@dataclass
class LocationDroppableItem:
    current: str
    location_items: list[LocationItem]

class LocationCard(ui.row):

    element_classes = 'flex w-full items-center mb-4'
    card_classes = 'flex-grow p-4 shadow-lg rounded-lg bg-white'
    button_classes = 'text-2xl font-mono'
    label_classes = 'text-2xl font-mono text-black'
    button_props = 'flat fab-mini no-caps'
    icon_size = 'md'
    selector_classes = f'{button_classes} text-center'
    drop_down_button_props = f'{button_props} borderless dropdown-icon="arrow_downward"'

    def __init__(self, items: list[ LocationDroppableItem | LocationItem ]) -> None:
        super().__init__()
    
        self.classes(self.element_classes)

        with self:
            with ui.card().classes('flex-none mr-4 shadow-lg rounded-lg bg-white items-center'):
                with ui.button(on_click=lambda: ui.navigate.back()).props(self.button_props):
                    ui.icon('arrow_back', size='md', color='blue-400')

            with ui.card().classes(self.card_classes):
                with ui.row().classes('items-center'):
                    with ui.button(on_click=lambda: ui.navigate.to('/')).props(self.button_props):
                        ui.icon('home', size='md', color='blue-400')
                    for item in items:
                        ui.icon('chevron_right', size=self.icon_size, color='blue')
                        if isinstance(item, LocationItem):
                            if item.navigate_to:
                                ui.button(item.label, on_click=lambda x, item=item: ui.navigate.to(item.navigate_to)) \
                                    .classes(self.button_classes).props(self.button_props)
                            else:
                                ui.label(item.label).classes(self.label_classes)
                            
                        elif isinstance(item, LocationDroppableItem):
                            options = [location_item.label for location_item in item.location_items]
                            options.sort()

                            with ui.dropdown_button(text=item.current,value=item.current, auto_close=True).classes(self.button_classes).props(self.drop_down_button_props):
                                for location_item in item.location_items:
                                    ui.item(location_item.label, on_click=lambda x, item=location_item: ui.navigate.to(item.navigate_to))

                            # ui.select(value=item.current, options=options, with_input=True,
                            #           on_change=lambda x, items=item.location_items: self.on_change(x.value, items)) \
                            #     .classes(self.selector_classes).props(self.selector_props)

    def on_change(self, x: str, items: list[LocationItem]):
        for item in items:
            if item.label == x:
                ui.navigate.to(item.navigate_to)