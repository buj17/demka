from PySide6.QtWidgets import QMainWindow

import database
import gui.ui.main_window_ui
from gui.widgets import LoginWidget
from gui.widgets.order_list_widget import OrderListWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = gui.ui.main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.clear_all_widgets()

        self.login_widget = LoginWidget(self)
        self.login_widget.setVisible(False)

        session = database.create_session()
        self.item_list_client_widget = OrderListWidget(self)
        session.close()

        self.ui.stackedWidget.addWidget(self.item_list_client_widget)

    def clear_all_widgets(self):
        for _ in range(self.ui.stackedWidget.count()):
            widget = self.ui.stackedWidget.widget(0)
            self.ui.stackedWidget.removeWidget(widget)
