from PySide6.QtWidgets import QWidget

import database.models
import gui.ui.item_card_widget_ui


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
            f'Количество на складе {self.item.stock_quantity}',
        )
        self.ui.item_current_discount_label.setText(
            f'Скидка: {self.item.current_discount}%',
        )

        if item.current_discount > 15:
            self.ui.item_current_discount_label.setStyleSheet(
                'QLabel { background-color: #2E8B57; }',
            )
