from nicegui import ui


class FilterInput(ui.input):
    width = 'w-80'

    color = 'blue'
    main_color = f'bg-{color}-200'
    round_size = '3xl'
    text_size = 'lg'
    text_color = 'black'
    icon_size = 'sm'

    filter_input_classes = f'''
        px-4 
        {main_color} 
        {width}
        text-{text_size} 
        text-{text_color} 
        rounded-{round_size} 
        shadow-inner
    '''

    def __init__(self, placeholder: str) -> None:

        super().__init__(placeholder=placeholder)
        self.classes(self.filter_input_classes)
        self.props('borderless')

        with self:
            with self.add_slot('prepend'):
                ui.icon('search', color=self.color, size=self.icon_size)