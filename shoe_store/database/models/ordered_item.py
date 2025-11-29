import sqlalchemy.orm

from database.models import Base


class OrderedItem(Base):
    __tablename__ = 'ordered_items'
    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True,
    )
    order_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('orders.id'),
    )
    item_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('items.id'),
    )
    item_count = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False,
        default=1,
    )

    order = sqlalchemy.orm.relationship(
        'Order',
        back_populates='ordered_items',
    )
    item = sqlalchemy.orm.relationship(
        'Item',
        back_populates='ordered_items',
    )

    __table_args__ = (
        sqlalchemy.UniqueConstraint(
            'order_id',
            'item_id',
            name='_order_item_uc',
        ),
    )
