from investbook.app.front.index import Main
from investbook.app.front.indices import Indices
from investbook.app.front.info import Info

from nicegui import ui


Main()
Indices()
Info()

ui.run(host="0.0.0.0", port=8080)
