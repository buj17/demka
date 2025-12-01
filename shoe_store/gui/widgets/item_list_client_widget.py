from PySide6.QtWidgets import QWidget

import database
from database.models import Item
import gui.ui.item_list_client_widget_ui
from gui.widgets.item_card_widget import ItemCardWidget
import gui.windows.main_window


class ItemListClientWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = gui.ui.item_list_client_widget_ui.Ui_Form()
        self.ui.setupUi(self)
        self.parent_widget: gui.windows.main_window.MainWindow
        self.parent_widget = self.parentWidget()

        session = database.create_session()

        for item in session.query(Item).all():
            self.ui.item_cards_layout.addWidget(ItemCardWidget(item))

        session.close()
