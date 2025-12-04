from PySide6.QtWidgets import QMessageBox, QWidget

import database
from database.models import User, UserRoleEnum
from gui.current_user import CurrentUser
import gui.ui.login_widget_ui
import gui.windows.main_window


class LoginWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = gui.ui.login_widget_ui.Ui_Form()
        self.ui.setupUi(self)
        self.parent_widget: gui.windows.main_window.MainWindow
        self.parent_widget = self.parent()

        self.ui.login_button.clicked.connect(self.login)
        self.ui.login_as_guest_button.clicked.connect(self.login_as_guest)

    def login(self):
        email = self.ui.login_line_edit.text()
        password = self.ui.password_line_Edit.text()

        with database.create_session() as session:
            query = session.query(User)
            user: User | type[User] = query.filter(User.email == email).first()

        if user is None or user.password != password:
            self.show_incorrect_login_error_message()
            return

        CurrentUser.set_current_user(user)
        self.close()

        new_widget = QWidget()
        if user.user_role == UserRoleEnum.AUTHORIZED_CLIENT:
            new_widget = gui.widgets.ItemListClientWidget(self.parent_widget)
        elif user.user_role == UserRoleEnum.MANAGER:
            new_widget = gui.widgets.ItemListManagerWidget(self.parent_widget)
        elif user.user_role == UserRoleEnum.ADMINISTRATOR:
            new_widget = gui.widgets.ItemListAdministratorWidget(
                self.parent_widget,
            )

        self.parent_widget.switch_widget(new_widget)

    def show_incorrect_login_error_message(self):
        QMessageBox.critical(
            self,
            'Ошибка',
            'Неверное имя пользователя или пароль',
            QMessageBox.StandardButton.Ok,
        )

    def login_as_guest(self):
        self.close()
        new_widget = gui.widgets.ItemListClientWidget(self.parent_widget)
        self.parent_widget.switch_widget(new_widget)
