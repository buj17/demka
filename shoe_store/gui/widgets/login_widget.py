from PySide6.QtWidgets import QWidget

import gui.ui.login_widget_ui


class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = gui.ui.login_widget_ui.Ui_Form()
        self.ui.setupUi(self)
