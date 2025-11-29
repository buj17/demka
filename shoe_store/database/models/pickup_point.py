import sqlalchemy

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
