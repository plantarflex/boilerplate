import os
import pathlib
from datetime import datetime, timedelta
import time
from threading import Threadi, Lock
from concurrent.futures import ThreadPoolExecutor

from models import *
from clients import Client
from manage import init_db, connect_db
from logger import Logger
from config import BaseConfig

from sqlalchemy.orm import sessionmaker


def init_demon():
    global logger
    logger = Logger()
    init_db(BaseConfig.DB_URI)


def thread_work(thread_name, lock):
    logger.create(thread_name)
    logger[thread_name].info('started')
    while True:
        lock.acquire()
        logger[thread_name].info('job started')
        lock.release()
        logger[thread_name].info('job finished')

def run():
    lock = Lock()
    with ThreadPoolExecutor as executor:
        for idx in range(1, BaseConfig.THREAD_WORKERS_NUM+1):
            executor.submit(idx, lock)


def run_accordingly():
    thread_1 = Thread(target=thread_work, args=(1,))
    thread_1.start()
    thread_1.join()


if __name__=='__main__':
    try:
        init_demon()
    except Exception as e:
        print('>>>>>>>> Demon initiation error')
    else:
        run()
