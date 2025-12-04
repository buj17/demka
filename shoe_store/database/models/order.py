import datetime

import sqlalchemy.orm

from database.models import Base


class Order(Base):
    __tablename__ = 'orders'
    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True,
    )
    order_date = sqlalchemy.Column(
        sqlalchemy.DateTime,
        nullable=False,
        default=datetime.datetime.now,
    )
    deliver_date = sqlalchemy.Column(
        sqlalchemy.DateTime,
    )
    pickup_point_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('pickup_points.id'),
    )
    user_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        sqlalchemy.ForeignKey('users.id'),
    )
    get_code = sqlalchemy.Column(
        sqlalchemy.Integer,
        nullable=False,
        default=0,
    )
    order_status = sqlalchemy.Column(
        sqlalchemy.String(256),
        nullable=False,
        default='',
    )

    pickup_point = sqlalchemy.orm.relationship(
        'PickupPoint',
        back_populates='orders',
    )
    user = sqlalchemy.orm.relationship(
        'User',
        back_populates='orders',
    )
    ordered_items = sqlalchemy.orm.relationship(
        'OrderedItem',
        back_populates='order',
    )

    def get_order_article(self):
        res = []
        for ordered_item in self.ordered_items:
            res.extend(
                (
                    ordered_item.item.article_number,
                    ordered_item.item_count,
                ),
            )
        return ', '.join(map(str, res))
