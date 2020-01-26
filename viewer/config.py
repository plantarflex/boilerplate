import sys
import os
from dotenv import load_dotenv
from datetime import timedelta

basedir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(basedir, '../.env')
load_dotenv(dotenv_path=env_path)


class Config(object):
    VERSION = os.environ['VERSION']
    SECRET_KEY = os.environ['SECRET_KEY']
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_SERVICE = os.environ['DB_SERVICE']
    DB_PORT = os.environ['DB_PORT']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(int(os.environ[
        'SQLALCHEMY_TRACK_MODIFICATIONS'
    ]))
    WEB_PORT = os.environ['WEB_PORT']
