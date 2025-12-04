from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLayout, QMessageBox, QWidget
import sqlalchemy
from sqlalchemy.orm import Query

import database
from database.models import Item
from gui.current_user import CurrentUser
import gui.ui.item_list_administrator_widget_ui
from gui.widgets.item_card_widget import ItemCardWidget
from gui.windows.item_add_form_window import ItemAddFormWindow
import gui.windows.main_window

_ALL_SUPPLIERS = 'Все поставщики'
_ORDER_ASC = 'По возрастанию'
_ORDER_DESC = 'По убыванию'


class ItemListAdministratorWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = gui.ui.item_list_administrator_widget_ui.Ui_Form()
        self.ui.setupUi(self)
        self.parent_widget: gui.windows.main_window.MainWindow
        self.parent_widget = self.parentWidget()

        self.items: list[Item] = []
        self.item_cards: list[ItemCardWidget] = []
        self.load_suppliers()

        self.refresh_items()

        self.ui.search_suppliers_combo_box.currentIndexChanged.connect(
            self.refresh_items,
        )
        self.ui.search_items_line_edit.textChanged.connect(
            self.refresh_items,
        )
        self.ui.sort_by_stock_quantity_combo_box.currentIndexChanged.connect(
            self.refresh_items,
        )

        self.set_full_name()

        self.ui.logout_button.clicked.connect(self.logout)
        self.ui.add_item_button.clicked.connect(self.open_add_item_form)

    def set_full_name(self):
        current_user = CurrentUser.get_current_user()
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

    def load_suppliers(self):
        self.ui.search_suppliers_combo_box.clear()
        self.ui.search_suppliers_combo_box.addItem(_ALL_SUPPLIERS)

        statement = sqlalchemy.select(
            sqlalchemy.distinct(
                Item.supplier,
            ),
        )
        with database.create_session() as session:
            result = session.execute(statement).fetchall()

        for supplier in map(lambda row: row[0], result):
            self.ui.search_suppliers_combo_box.addItem(supplier)

    def refresh_items(self):
        self.items.clear()
        self.item_cards.clear()
        clear_layout(self.ui.item_cards_layout)

        search_text = self.ui.search_items_line_edit.text()
        supplier = self.ui.search_suppliers_combo_box.currentText()
        sort_param = self.ui.sort_by_stock_quantity_combo_box.currentText()

        with database.create_session() as session:
            query: Query[Item | type[Item]] = session.query(Item)
            if search_text:
                query = query.filter(
                    sqlalchemy.or_(
                        Item.name.ilike(f'%{search_text}%'),
                        Item.producer.ilike(f'%{search_text}%'),
                        Item.supplier.ilike(f'%{search_text}%'),
                        Item.description.ilike(f'%{search_text}%'),
                        Item.article_number.ilike(f'%{search_text}%'),
                        Item.category.ilike(f'%{search_text}%'),
                    ),
                )

            if supplier != _ALL_SUPPLIERS:
                query = query.filter(
                    Item.supplier.ilike(supplier),
                )

            if sort_param == _ORDER_ASC:
                query = query.order_by(Item.stock_quantity)
            elif sort_param == _ORDER_DESC:
                query = query.order_by(sqlalchemy.desc(Item.stock_quantity))

            self.items.extend(query.all())

        for item in self.items:
            self.ui.item_cards_layout.addWidget(
                ItemCardWidget(
                    item,
                    self,
                ),
            )

    def open_add_item_form(self):
        add_item_form = ItemAddFormWindow(self)
        add_item_form.setWindowModality(Qt.WindowModality.ApplicationModal)
        add_item_form.show()
        add_item_form.exec()
        self.refresh_items()


def clear_layout(layout: QLayout):
    while layout.count():
        q_obj = layout.takeAt(0)
        widget = q_obj.widget()
        if widget is not None:
            widget.deleteLater()
        else:
            sublayout = q_obj.layout()
            if sublayout is not None:
                clear_layout(sublayout)
