import sys
import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta, datetime

basedir = os.path.dirname(os.path.abspath(__file__))
env_path = Path(os.path.join(basedir, "..")) / '.env'
load_dotenv(dotenv_path=env_path)


if False in [sys.platform == "linux", sys.platform == "linux2"]:
    os.environ['DB_SERVICE'] = "localhost"


class Config(object):
    THREAD_WORKERS_NUM = int(os.environ['THREAD_WORKERS_NUM'])
    LOG_FILE_SIZE = int(os.environ['LOG_FILE_SIZE'])
    VIEWER_PORT = int(os.environ['VIEWER_PORT'])

    VIKI_DB_NAME = os.environ['VIKI_DB_NAME']
    VIKI_DB_USER = os.environ['VIKI_DB_USER']
    VIKI_DB_PASS = os.environ['VIKI_DB_PASS']
    VIKI_DB_SERVICE = os.environ['VIKI_DB_SERVICE']
    VIKI_DB_PORT = os.environ['VIKI_DB_PORT']
    VIKI_DB_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        VIKI_DB_USER, VIKI_DB_PASS, VIKI_DB_SERVICE, VIKI_DB_PORT, VIKI_DB_NAME)

    VIEWER_DB_NAME = os.environ['VIEWER_DB_NAME']
    VIEWER_DB_USER = os.environ['VIEWER_DB_USER']
    VIEWER_DB_PASS = os.environ['VIEWER_DB_PASS']
    VIEWER_DB_SERVICE = os.environ['VIEWER_DB_SERVICE']
    VIEWER_DB_PORT = os.environ['VIEWER_DB_PORT']
    VIEWER_DB_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        VIEWER_DB_USER, VIEWER_DB_PASS, VIEWER_DB_SERVICE, VIEWER_DB_PORT, VIEWER_DB_NAME)

    SQLALCHEMY_DATABASE_URI = VIEWER_DB_URI
    SQLALCHEMY_BINDS = {'viki': VIKI_DB_URI }
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(int(
        os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']))
