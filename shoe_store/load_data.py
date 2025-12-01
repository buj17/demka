from typing import Sequence

import sqlalchemy

import config.settings
import data_loader
import database.models

_USER_XLSX_FILE = (
    config.settings.BASE_DIR / 'import_data' / 'user_import.xlsx'
)
_PICKUP_POINT_XLSX_FILE = (
    config.settings.BASE_DIR / 'import_data' / 'pickup_point_import.xlsx'
)
_ITEM_XLSX_FILE = (
    config.settings.BASE_DIR / 'import_data' / 'item_import.xlsx'
)
_ORDER_XLSX_FILE = (
    config.settings.BASE_DIR / 'import_data' / 'order_import.xlsx'
)


def prepare_user_dict(
    users: Sequence[database.models.User]
) -> dict[str, database.models.User]:
    res = {}
    for user in users:
        full_name = ' '.join((user.last_name, user.first_name, user.surname))
        res[full_name] = user
    return res

def prepare_item_dict(
    items: Sequence[database.models.Item]
) -> dict[str, database.models.Item]:
    res = {}
    for item in items:
        res[item.article_number] = item
    return res

if __name__ == '__main__':
    session = database.create_session()

    # Truncate all existing data
    with database.connect.engine.connect() as connection:
        with connection.begin():
            for table in reversed(database.models.Base.metadata.sorted_tables):
                truncate_statement = (
                    f'TRUNCATE TABLE {table.name} RESTART IDENTITY CASCADE;'
                )
                connection.execute(
                    sqlalchemy.text(truncate_statement)
                )

    users = data_loader.parse_users(
        _USER_XLSX_FILE,
    )
    session.add_all(users)
    session.flush()
    print('Loaded users to database')

    pickup_points = data_loader.parse_pickup_points(
        _PICKUP_POINT_XLSX_FILE,
    )
    session.add_all(pickup_points)
    session.flush()
    print('Loaded pickup points to database')

    items = data_loader.parse_items(
        _ITEM_XLSX_FILE,
    )
    session.add_all(items)
    session.flush()
    print('Loaded items to database')

    data_loader.parse_orders(
        _ORDER_XLSX_FILE,
        session,
        user_dict=prepare_user_dict(users),
        item_dict=prepare_item_dict(items),
        pickup_points=pickup_points,
    )
    print('Loaded orders to database')

    print('All objects loaded to database')

    session.commit()

    session.close()
