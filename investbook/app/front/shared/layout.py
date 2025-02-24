from investbook.app.front.components.layout.header import Header

class Layout:

    def __init__(self, usuario_actual) -> None:
        self.header = Header(usuario_actual)  # Pasamos el usuario actual al Header
