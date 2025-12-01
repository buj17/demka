from PySide6.QtWidgets import QMessageBox, QWidget

import gui.ui.login_widget_ui
import gui.windows.main_window


class LoginWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = gui.ui.login_widget_ui.Ui_Form()
        self.ui.setupUi(self)
        self.parent_widget: gui.windows.main_window.MainWindow
        self.parent_widget = self.parentWidget()

        self.ui.login_button.clicked.connect(self.login)
        self.ui.login_as_guest_button.clicked.connect(self.login_as_guest)

    def login(self):
        email = self.ui.login_line_edit.text()
        password = self.ui.password_line_Edit.text()
        print(email, password)

    def show_incorrect_login_error_message(self):
        QMessageBox.critical(
            self,
            'Ошибка',
            'Неверное имя пользователя или пароль',
            QMessageBox.StandardButton.Ok,
        )

    def login_as_guest(self):
        print('login as guest')
