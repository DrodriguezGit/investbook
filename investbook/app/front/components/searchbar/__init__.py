from __future__ import annotations
from dataclasses import dataclass, field

from nicegui import ui
from nicegui.events import KeyEventArguments
from nicegui.observables import ObservableList

@dataclass
class DataSet:
    data: list
    field: str
    rt_prefix: str
    icon: str = None
    icon_url: str = None

@dataclass
class SearchManager:
    active_idx: int = -1
    results: list[SearchResult] = field(default_factory=list)

@dataclass
class SearchResult:
    label: str
    navigate_to: str
    obj: ui.button = None
    icon: str = None
    icon_url: str = None

@dataclass
class SearchStyle:
    color: str
    text_color: str
    text_size_input: str
    text_size_results: str
    round_size: str
    icon_size: str


class SearchBar:

    def __init__(self, title: str, source_data: list[DataSet], style: SearchStyle, max_search: int) -> None:

        self.data_manager = source_data
        self.max_search = max_search

        self._styles(style)
        
        self.smanager = SearchManager()

        self.keyboard = ui.keyboard(on_key=lambda e: self.handle_key(e), active=False, ignore=[])

        search_bar_position = 'absolute inset-0 justify-center items-center'
        results_position = 'absolute left-0 right-0 top-1/2 mt-16 items-center'

        with ui.column().classes(search_bar_position):
            ui.label(title).classes(self.title_classes)

            with ui.input(on_change=lambda text: self.find(text.value)).classes(self.search_bar_classes).props('borderless') as self.search_bar:
                with self.search_bar.add_slot('prepend'):
                    ui.icon('search', color=self.icon_color, size=self.icon_size)
            
        with ui.column().classes(results_position) as self.results_container:
            pass
    
    def _styles(self, style: SearchStyle):

        self.widths = 'w-5/6 sm:w-2/3 md:w-1/3'

        self.color = style.color
        self.round_size = style.round_size

        self.icon_size = style.icon_size
        self.icon_color = style.color

        self.main_color = f'bg-{style.color}-200'
        self.hover_color = f'bg-{style.color}-300' 

        self.text_color = style.text_color
        self.text_size_input = style.text_size_input
        self.text_size_results = style.text_size_results
        
        self.title_classes = f'text-5xl font-extrabold mb-4 text-center text-{self.color}'

        self.search_bar_classes = f'''
            px-4 
            {self.main_color} 
            {self.widths}
            text-{self.text_size_input} 
            text-{self.text_color} 
            rounded-{self.round_size} 
            shadow-inner
        '''

        self.search_result_classes = f'''
            -mb-4 
            {self.main_color} 
            {self.widths}
            justify-center 
            text-{self.text_size_results} 
            text-{self.text_color} 
            shadow-x-inner 
            hover:{self.hover_color}
            rounded-none
        '''

        self.footer_classes = f'''
            {self.main_color}
            {self.widths}
            justify-center 
            shadow-none 
            rounded-b-{self.round_size} 
            rounded-t-none
        '''
        self.not_found_classes = f'''
            {self.main_color} 
            {self.widths}
            justify-center 
            text-{self.text_size_results} 
            text-{self.text_color} 
            shadow-none 
            rounded-b-{self.round_size} 
            rounded-t-none
        '''
        
    async def find(self, text: str):

        self.results_container.clear()
        self.smanager.active_idx = -1

        if text:
            self.smanager.results.clear()
            for dataset in self.data_manager:
                for item in dataset.data:
                    label: str = getattr(item, dataset.field)
                    if text.lower() in label.lower():
                        sr = SearchResult(
                            label=label,
                            ## TODO: revisar cómo pasar esto
                            navigate_to=f'{dataset.rt_prefix}/{label}',
                            icon=dataset.icon,
                            icon_url=dataset.icon_url
                        )
                        self.smanager.results.append(sr)
            
            self.search_bar.classes(remove=f'rounded-{self.round_size}', add=f'rounded-t-{self.round_size}')

            if self.smanager.results:

                self.keyboard.active = True

                with self.results_container:

                    for sr in self.smanager.results[:self.max_search]:
                        with ui.button(on_click=lambda: ui.navigate.to(sr.navigate_to)) \
                            .classes(self.search_result_classes).props('flat align="left"') as sr.obj:
                            if sr.icon_url:
                                ui.image(sr.icon_url).classes("w-4 h-4 mr-3") 
                            else:
                                ui.icon(sr.icon or 'search', size=self.icon_size, color=self.icon_color).classes('mr-3')
                            ui.label(sr.label).classes()

                            async def mousemove():
                                if self.smanager.active_idx >=0:
                                    await self.unfocus()
                                await self.reset_focus()

                            sr.obj.on('mousemove', mousemove)

                    with ui.card().classes(self.footer_classes):
                        ui.label('powered by TripleAlpha').classes('w-full text-center text-xs text-orange-600')

            else:

                self.keyboard.active = False

                with self.results_container:

                    with ui.card().classes(self.not_found_classes):
                        with ui.row():
                            ui.icon('sentiment_dissatisfied', size=self.icon_size, color=self.icon_color).classes('-mr-1')
                            ui.label('No se encontraron resultados')
        else:
            
            self.keyboard.active = False
            self.search_bar.classes(remove=f'rounded-t-{self.round_size}', add=f'rounded-{self.round_size}')
    
    async def focus(self):
        self.smanager.results[self.smanager.active_idx].obj.classes(remove=self.main_color, add=self.hover_color)
    
    async def unfocus(self):
        self.smanager.results[self.smanager.active_idx].obj.classes(remove=self.hover_color, add=self.main_color)
    
    async def reset_focus(self):
        self.smanager.active_idx = -1

    async def handle_key(self, e: KeyEventArguments):

        if self.smanager.results and e.action.keydown:

            last_result_idx = len(self.smanager.results) - 1

            if e.key.arrow_down:

                if self.smanager.active_idx < 0:
                    self.smanager.active_idx += 1
                    await self.focus()

                elif 0 <= self.smanager.active_idx < last_result_idx:
                    await self.unfocus()
                    self.smanager.active_idx += 1
                    await self.focus()
        
            if e.key.arrow_up:

                if self.smanager.active_idx == 0:
                    await self.unfocus()
                    self.smanager.active_idx -= 1

                if 0 < self.smanager.active_idx <= last_result_idx:
                    await self.unfocus()
                    self.smanager.active_idx -= 1
                    await self.focus()
            
            if e.key.enter:

                if self.smanager.active_idx >= 0:
                    ui.navigate.to(self.smanager.results[self.smanager.active_idx].navigate_to)