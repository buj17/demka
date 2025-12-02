import os
import pathlib

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import sqlalchemy.orm

import config.settings
from database.models.base import Base

_DEFAULT_IMAGE_FILENAME = 'picture.png'
_IMAGE_WIDTH = 200
_IMAGE_HEIGHT = 150


class Item(Base):
    __tablename__ = 'items'
    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True,
    )
    article_number = sqlalchemy.Column(
        sqlalchemy.String(6),
        unique=True,
    )
    name = sqlalchemy.Column(
        sqlalchemy.String(256),
        nullable=False,
        default='',
    )
    price = sqlalchemy.Column(
        sqlalchemy.Numeric(10, 2),
        nullable=False,
        default=0,
    )
    supplier = sqlalchemy.Column(
        sqlalchemy.String(256),
        nullable=False,
        default='',
    )
    producer = sqlalchemy.Column(
        sqlalchemy.String(256),
        nullable=False,
        default='',
    )
    category = sqlalchemy.Column(
        sqlalchemy.String(256),
        nullable=False,
        default='',
    )
    current_discount = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False,
        default=0,
    )
    measure = sqlalchemy.Column(
        sqlalchemy.String(256),
        nullable=False,
        default='',
    )
    stock_quantity = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False,
        default=0,
    )
    description = sqlalchemy.Column(
        sqlalchemy.Text,
        nullable=False,
        default='',
    )
    image_filename = sqlalchemy.Column(
        sqlalchemy.String(256),
        nullable=False,
        default=_DEFAULT_IMAGE_FILENAME,
    )

    ordered_items = sqlalchemy.orm.relationship(
        'OrderedItem',
        back_populates='item',
    )

    @sqlalchemy.orm.validates('price')
    def validate_price(self, key, value):
        if value < 0:
            raise ValueError('Price cannot be negative')

        if isinstance(value, float):
            return round(value, 2)

        return value

    @sqlalchemy.orm.validates('current_discount')
    def validate_discount(self, key, value):
        if not 0 <= value <= 100:
            raise ValueError('Discount must be in range [0; 100]')

        return value

    @sqlalchemy.orm.validates('stock_quantity')
    def validate_stock_quantity(self, key, value):
        if value < 0:
            raise ValueError('Quantity cannot be negative')

        return value

    def get_image(self, width: int, height: int) -> QPixmap:
        image = QPixmap(
            config.settings.BASE_DIR / 'media' / self.image_filename,
        )

        return image.scaled(
            _IMAGE_WIDTH,
            _IMAGE_HEIGHT,
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

    def set_image(self, image_path: str | pathlib.Path):
        previous_file = self.image_filename

        self.image_filename = f'{self.id}.jpg'

        image = QPixmap(image_path)
        scaled_image = image.scaled(
            _IMAGE_WIDTH,
            _IMAGE_HEIGHT,
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        scaled_image.save(
            str(config.settings.BASE_DIR / 'media' / self.image_filename),
        )

        if (previous_file != _DEFAULT_IMAGE_FILENAME
            and previous_file != self.image_filename):
            os.remove(
                config.settings.BASE_DIR / 'media' / previous_file,
            )

    def get_reduced_price(self):
        return round(
            self.price - self.current_discount * self.price / 100,
            2,
        )
