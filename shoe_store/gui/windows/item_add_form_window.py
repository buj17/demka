from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
import sqlalchemy

import config.settings
import database
from database.models import Item
from database.models.item import DEFAULT_IMAGE_HEIGHT, DEFAULT_IMAGE_WIDTH
import gui.ui.item_add_form_window_ui
import gui.windows.main_window


class ItemAddFormWindow(QDialog):
    def __init__(self, *args, item: Item | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = gui.ui.item_add_form_window_ui.Ui_Form()
        self.ui.setupUi(self)
        self.parent_widget: gui.windows.main_window.MainWindow
        self.parent_widget = self.parentWidget()

        self.setWindowTitle('Добавить товар')

        self.load_categories()
        self.load_producers()

        self.ui.item_upload_photo_button.clicked.connect(
            self.select_item_photo,
        )
        self.ui.submit_button.clicked.connect(
            self.save,
        )

        self.current_item_image: QPixmap | None = None

        self.item = item
        if self.item is not None:
            self.ui.item_image_label.setPixmap(
                self.item.get_image(),
            )
            self.ui.item_name_line_edit.setText(
                self.item.name,
            )
            self.ui.item_category_combo_box.setCurrentText(
                self.item.category,
            )
            self.ui.item_description_plain_text_edit.setPlainText(
                self.item.description,
            )
            self.ui.item_producer_combo_box.setCurrentText(
                self.item.producer,
            )
            self.ui.item_supplier_line_edit.setText(
                self.item.supplier,
            )
            self.ui.item_price_double_spin_box.setValue(
                float(self.item.price),
            )
            self.ui.item_measure_line_edit.setText(
                self.item.measure,
            )
            self.ui.item_stock_quantity_spin_box.setValue(
                self.item.stock_quantity,
            )
            self.ui.item_current_discount_spin_box.setValue(
                self.item.current_discount,
            )
        else:
            default_image = QPixmap(
                config.settings.BASE_DIR / 'media' / 'picture.png',
            )
            self.ui.item_image_label.setPixmap(default_image)

    def load_categories(self):
        self.ui.item_category_combo_box.clear()

        statement = sqlalchemy.select(
            sqlalchemy.distinct(
                Item.category,
            ),
        )
        with database.create_session() as session:
            result = session.execute(statement).fetchall()

        for category in map(lambda row: row[0], result):
            self.ui.item_category_combo_box.addItem(category)

    def load_producers(self):
        self.ui.item_producer_combo_box.clear()

        statement = sqlalchemy.select(
            sqlalchemy.distinct(
                Item.producer,
            ),
        )
        with database.create_session() as session:
            result = session.execute(statement).fetchall()

        for producer in map(lambda row: row[0], result):
            self.ui.item_producer_combo_box.addItem(producer)

    def select_item_photo(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self,
            'Загрузить изображение',
            '',
            'Image Files (*.png *.jpg *.jpeg *.bmp *.gif)',
        )
        if file_path:
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                scaled = pixmap.scaled(
                    DEFAULT_IMAGE_WIDTH,
                    DEFAULT_IMAGE_HEIGHT,
                    Qt.AspectRatioMode.IgnoreAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
                self.ui.item_image_label.setPixmap(scaled)
                self.current_item_image = scaled
            else:
                QMessageBox.critical(
                    self,
                    'Ошибка',
                    'Не удалось загрузить изображение',
                )

    def save(self):
        if self.item:
            item = self.item
        else:
            item = Item()

        with database.create_session() as session:
            session.add(item)

            item.name = self.ui.item_name_line_edit.text()
            item.category = self.ui.item_category_combo_box.currentText()
            item.description = (
                self.ui.item_description_plain_text_edit.toPlainText()
            )
            item.producer = self.ui.item_producer_combo_box.currentText()
            item.supplier = self.ui.item_supplier_line_edit.text()
            item.set_price(self.ui.item_price_double_spin_box.value())
            item.measure = self.ui.item_measure_line_edit.text()
            item.stock_quantity = (
                self.ui.item_stock_quantity_spin_box.value()
            )
            item.current_discount = (
                self.ui.item_current_discount_spin_box.value()
            )
            if self.current_item_image:
                item.set_image_from_pixmap(self.current_item_image)
            session.commit()

        QMessageBox.information(
            self,
            'Успешно',
            'Данные успешно сохранены',
        )
        self.close()
