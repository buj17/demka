from PySide6.QtWidgets import QLayout, QWidget
import sqlalchemy.orm
from sqlalchemy.orm import Query

import database
from database.models import Order, OrderedItem
import gui.ui.order_list_manager_widget_ui
from gui.widgets.order_card_widget import OrderCardWidget
import gui.windows.main_window


class OrderListWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = gui.ui.order_list_widget_ui.Ui_Form()
        self.ui.setupUi(self)
        self.parent_widget: gui.windows.main_window.MainWindow
        self.parent_widget = self.parentWidget()

        self.orders: list[Order] = []
        self.order_cards: list[OrderCardWidget] = []

        self.refresh_orders()

    def refresh_orders(self):
        self.orders.clear()
        self.order_cards.clear()
        clear_layout(self.ui.order_cards_layout)

        with database.create_session() as session:
            query: Query[Order | type[Order]] = session.query(Order)

            query = query.options(
                (
                    sqlalchemy.orm.selectinload(Order.ordered_items)
                    .selectinload(OrderedItem.item)
                ),
                (
                    sqlalchemy.orm.joinedload(Order.pickup_point)
                ),
            )

            self.orders.extend(query.all())

        for order in self.orders:
            self.ui.order_cards_layout.addWidget(OrderCardWidget(order))


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
