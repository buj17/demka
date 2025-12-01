from PySide6.QtWidgets import QMainWindow

import gui.ui.main_window_ui
from gui.widgets import LoginWidget
from gui.widgets.item_list_client_widget import ItemListClientWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = gui.ui.main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.clear_all_widgets()

        self.login_widget = LoginWidget(self)
        self.login_widget.setVisible(False)

        self.item_list_client_widget = ItemListClientWidget(self)

        self.ui.stackedWidget.addWidget(self.item_list_client_widget)

    def clear_all_widgets(self):
        for _ in range(self.ui.stackedWidget.count()):
            widget = self.ui.stackedWidget.widget(0)
            self.ui.stackedWidget.removeWidget(widget)
