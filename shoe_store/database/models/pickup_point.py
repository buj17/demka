import sqlalchemy.orm

from database.models import Base


class PickupPoint(Base):
    __tablename__ = 'pickup_points'
    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True,
    )
    address = sqlalchemy.Column(
        sqlalchemy.String(256),
    )
    orders = sqlalchemy.orm.relationship(
        'Order',
        back_populates='pickup_point',
    )
