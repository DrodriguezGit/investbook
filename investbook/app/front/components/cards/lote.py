from __future__ import annotations
from nicegui import ui

from webapp.front.components.cards.base import BaseCard, BaseCardItem, BaseCardElement


class LoteCard(BaseCard):

    def __init__(self, id_lote: str, duracion: int, id_granja: str, num_animales: int, fases: list) -> None:

        super().__init__(
            title=f'Lote {id_lote}',
            main_card_element=BaseCardElement(id=id_lote, description='lote'),
            card_items=[
                BaseCardItem(icon='home',text=id_granja),
                BaseCardItem(icon='timelapse',text=duracion),
                BaseCardItem(icon='info',text=num_animales),
            ]
        )
        
        with self:
            with ui.row().classes('w-full justify-center'):
                with ui.dropdown_button('Ver informes', icon='visibility') \
                    .classes(self.navigation_button_classes).props(self.navigation_button_props):
                    for fase in fases:
                        ui.item(f'Fase {fase}', on_click=lambda fase=fase: ui.navigate.to(f'{id_lote}/{fase}/informes'))