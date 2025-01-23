from nicegui import ui


class TitleLabel(ui.row):
    
    title_classes = 'items-end'
    icon_size = 'sm'
    icon_color = 'slate-600'
    label_classes = 'text-xl text-slate-600 font-mono'

    def __init__(self, text: str, icon: str=None) -> None:
        
        super().__init__()
        self.classes(self.title_classes)

        with self:
            if icon: ui.icon(icon, size=self.icon_size, color=self.icon_color)
            ui.label(text).classes(self.label_classes)

class TitleReport(ui.row):

    title_classes = 'relative w-full items-center justify-center'

    def __init__(self, text: str) -> None:

        super().__init__()
        self.classes(self.title_classes)
        with self:
            # ui.icon('sym_r_stack', size='xl', color='slate-600')
            ui.label(text).classes('text-4xl mb-4 text-slate-600 font-mono')