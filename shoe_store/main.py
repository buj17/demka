import sqlalchemy

from database.connect import create_session

session = create_session()
print(
    session.execute(
        sqlalchemy.text('SELECT version();'),
    ).fetchall(),
)
