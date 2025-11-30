from PySide6.QtWidgets import QMainWindow

import gui.ui.main_window_ui
from gui.widgets import LoginWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = gui.ui.main_window_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.clear_all_widgets()

        self.login_widget = LoginWidget()
        self.ui.stackedWidget.addWidget(self.login_widget)

    def clear_all_widgets(self):
        for _ in range(self.ui.stackedWidget.count()):
            widget = self.ui.stackedWidget.widget(0)
            self.ui.stackedWidget.removeWidget(widget)
