from PySide6.QtWidgets import QWidget

import database.models
import gui.ui.order_card_widget_ui


class OrderCardWidget(QWidget):
    def __init__(
        self,
        order: database.models.Order,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.ui = gui.ui.order_card_widget_ui.Ui_Form()
        self.ui.setupUi(self)
        self.order = order

        self.ui.order_article_label.setText(
            f'Артикул: {self.order.get_order_article()}',
        )
        self.ui.order_status_label.setText(
            f'Статус: {self.order.order_status}',
        )
        self.ui.order_address_label.setText(
            f'Адрес пункта выдачи: {self.order.pickup_point.address}',
        )
        self.ui.order_date_label.setText(
            f'Дата заказа: {self.order.order_date.strftime('%d.%m.%Y')}',
        )
        self.ui.deliver_date_label.setText(
            f'Дата выдачи: {self.order.deliver_date.strftime('%d.%m.%Y')}',
        )
