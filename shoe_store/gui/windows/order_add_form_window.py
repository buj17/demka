from PySide6.QtWidgets import QWidget

from database.models import Order
import gui.ui.order_add_form_window_ui
import gui.windows.main_window


class ItemAddFormWindow(QWidget):
    def __init__(self, *args, order: Order | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = gui.ui.order_add_form_window_ui.Ui_Form()
        self.ui.setupUi(self)
        self.parent_widget: gui.windows.main_window.MainWindow
        self.parent_widget = self.parentWidget()
