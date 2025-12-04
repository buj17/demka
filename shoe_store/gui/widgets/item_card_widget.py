from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu, QMessageBox, QWidget

import database.models
from database.models import UserRoleEnum
from gui.current_user import CurrentUser
import gui.ui.item_card_widget_ui
from gui.windows.item_add_form_window import ItemAddFormWindow
import gui.windows.main_window


class ItemCardWidget(QWidget):
    def __init__(
        self,
        item: database.models.Item,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.ui = gui.ui.item_card_widget_ui.Ui_Form()
        self.ui.setupUi(self)
        self.item = item
        self.parent_widget: gui.widgets.ItemListAdministratorWidget
        self.parent_widget = self.parentWidget()

        self.ui.item_image_label.setText(
            '',
        )
        self.ui.item_image_label.setPixmap(
            self.item.get_image(200, 150),
        )
        self.ui.item_category_name_label.setText(
            f'{self.item.category} | {self.item.name}',
        )
        self.ui.item_description_label.setText(
            f'Описание: {self.item.description}',
        )
        self.ui.item_producer_label.setText(
            f'Производитель: {self.item.producer}',
        )
        self.ui.item_supplier_label.setText(
            f'Поставщик: {self.item.supplier}',
        )
        self.ui.item_price_label.setText(
            f'Цена: {self.item.price}',
        )
        self.ui.item_measure_label.setText(
            f'Единица измерения: {self.item.measure}',
        )
        self.ui.item_stock_quantity_label.setText(
            f'Количество на складе: {self.item.stock_quantity}',
        )
        self.ui.item_current_discount_label.setText(
            f'Скидка: {self.item.current_discount}%',
        )

        if item.current_discount > 0:
            self.ui.item_price_label.setText(
                f'Цена: '
                f'<span style="color: red;">'
                f'<s>'
                f'{self.item.price}'
                f'</s>'
                f'</span> '
                f'{self.item.get_reduced_price()}',
            )

        if item.current_discount > 15:
            self.ui.item_current_discount_label.setStyleSheet(
                'QLabel { background-color: #2E8B57; }',
            )

        if item.stock_quantity == 0:
            self.ui.item_stock_quantity_label.setText(
                '<span style="color: cyan;">'
                f'Количество на складе: {self.item.stock_quantity}'
                '</span>',
            )

    def mousePressEvent(self, event, /):
        current_user = CurrentUser.get_current_user()
        if (
            current_user is None
            or current_user.user_role != UserRoleEnum.ADMINISTRATOR
        ):
            return

        if event.button() == Qt.MouseButton.LeftButton:
            self.open_edit_item_form()
        elif event.button() == Qt.MouseButton.RightButton:
            menu = QMenu(self)
            delete_action = QAction('Удалить', self)
            delete_action.triggered.connect(self.delete_item)
            menu.addAction(delete_action)
            menu.exec(event.globalPos())

    def delete_item(self):
        reply = QMessageBox.question(
            self,
            'Подтвердить удаление',
            'Вы действительно хотите удалить данный товар?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            with database.create_session() as session:
                session.delete(self.item)
                session.commit()
            self.parent_widget.refresh_items()

    def open_edit_item_form(self):
        add_item_form = ItemAddFormWindow(
            self,
            item=self.item,
        )
        add_item_form.setWindowModality(Qt.WindowModality.ApplicationModal)
        add_item_form.show()
        add_item_form.exec()
        self.parent_widget.refresh_items()
