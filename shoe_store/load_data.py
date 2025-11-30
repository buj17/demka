import config.settings
import data_loader.load_users
import database.models

_USER_XLSX_FILE = (
    config.settings.BASE_DIR / 'import_data' / 'user_import.xlsx'
)

if __name__ == '__main__':
    session = database.create_session()

    session.query(database.models.User).delete()

    users = data_loader.load_users.parse_users(_USER_XLSX_FILE)
    session.add_all(users)
    session.flush()

    session.commit()

    session.close()
