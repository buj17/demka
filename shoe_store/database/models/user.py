import enum

import sqlalchemy

from database.models.base import Base


class UserRoleEnum(enum.Enum):
    ADMINISTRATOR = 'admin'
    AUTHORIZED_CLIENT = 'client'
    MANAGER = 'manager'


class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True,
    )
    role = sqlalchemy.Column(
        sqlalchemy.Enum(UserRoleEnum),
    )
    last_name = sqlalchemy.Column(
        sqlalchemy.String(256),
        nullable=False,
        default='',
    )
    first_name = sqlalchemy.Column(
        sqlalchemy.String(256),
        nullable=False,
        default='',
    )
    surname = sqlalchemy.Column(
        sqlalchemy.String(256),
        nullable=False,
        default='',
    )
    email = sqlalchemy.Column(
        sqlalchemy.String(256),
        unique=True,
        nullable=False,
        default='',
    )
    password = sqlalchemy.Column(
        sqlalchemy.String(256),
        nullable=False,
        default='',
    )
