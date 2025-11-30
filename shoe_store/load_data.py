import sqlalchemy

import config.settings
import data_loader.load_users
import data_loader.load_pickup_points
import database.models

_USER_XLSX_FILE = (
    config.settings.BASE_DIR / 'import_data' / 'user_import.xlsx'
)
_PICKUP_POINT_XLSX_FILE = (
    config.settings.BASE_DIR / 'import_data' / 'pickup_point_import.xlsx'
)

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

    users = data_loader.load_users.parse_users(_USER_XLSX_FILE)
    session.add_all(users)
    session.flush()

    pickup_points = data_loader.load_pickup_points.parse_pickup_points(
        _PICKUP_POINT_XLSX_FILE,
    )
    session.add_all(pickup_points)
    session.flush()

    session.commit()

    session.close()
