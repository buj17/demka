from PySide6.QtWidgets import QMessageBox, QWidget

import database
from database.models import Item
from gui.current_user import CurrentUser
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

        with database.create_session() as session:
            for item in session.query(Item).all():
                item: Item | type[Item]
                self.ui.item_cards_layout.addWidget(ItemCardWidget(item))

        self.set_full_name()

        self.ui.logout_button.clicked.connect(self.logout)

    def set_full_name(self):
        current_user = CurrentUser.get_current_user()
        if current_user is None:
            self.ui.full_name_label.setText('Гость')
            return

        self.ui.full_name_label.setText(current_user.get_full_name())

    def logout(self):
        reply = QMessageBox.question(
            self,
            'Подтвердить выход',
            'Вы действительно хотите выйти?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            CurrentUser.clear_current_user()
            self.close()
            new_widget = gui.widgets.LoginWidget(self.parent_widget)
            self.parent_widget.switch_widget(new_widget)
