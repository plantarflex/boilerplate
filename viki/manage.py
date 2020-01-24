import sqlalchemy
from sqlalchemy_utils import database_exists, create_database

from models import Base


def create_engine(uri):
    return sqlalchemy.create_engine(uri).connect()


def create_schema(engine):
    Base.metadata.create_all(engine)


def init_db(uri):
    if not database_exists(uri):
       print('>>>> Creating database...')
       create_database(uri)
       engine = create_engine(uri)
       print('>>>> Creating schema...')
       create_schema(engine)
    else:
        print('>>>> Database exists...')


def connect_db(uri):
    if not database_exists(uri):
        print('>>>> Database Not Found...')
        return
    else:
        print('>>>> DB Connecting...')
        engine = create_engine(uri)
    return engine


# TODO: add alembic for version control
