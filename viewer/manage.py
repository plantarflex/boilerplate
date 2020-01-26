from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from config import Config


def create_database():
    database_uri_without_db_name = Config.SQLALCHEMY_DATABASE_URI[
        :Config.SQLALCHEMY_DATABASE_URI.rfind('/')
    ]
    with db.create_engine(database_uri_without_db_name).connect() as conn:
        conn.execution_options(
            isolation_level='AUTOCOMMIT'
        ).execute('create database %s owner postgres'%(Config.DB_NAME))

try:
    db.create_engine(Config.SQLALCHEMY_DATABASE_URI).connect()
except Exception as e:
    print(e)
    create_database()

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
