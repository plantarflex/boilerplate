import os
import pathlib
from datetime import datetime, timedelta
import time
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor

from models import *
from clients import FileClient
from manage import init_db, connect_db
from logger import Logger
from config import Config

from sqlalchemy.orm import sessionmaker


def init_demon():
    global logger
    logger = Logger()
    init_db(Config.VIKI_DB_URI)


def thread_work(thread_idx, lock):
    logger.create(thread_idx)
    logger[thread_idx].info('started')
    while True:
        time.sleep(5)
        lock.acquire()
        logger[thread_idx].info('job started')
        lock.release()
        logger[thread_idx].info('job finished')


def run():
    lock = Lock()
    with ThreadPoolExecutor(max_workers=Config.THREAD_WORKERS_NUM) as executor:
        for idx in range(1, Config.THREAD_WORKERS_NUM+1):
            executor.submit(
                thread_work,
                str(idx),
                lock
                )


def run_accordingly():
    thread_1 = Thread(target=thread_work, args=(1,))
    thread_1.start()
    thread_1.join()


if __name__=='__main__':
    try:
        init_demon()
    except Exception as e:
        print('>>>>>>>> Demon initiation error')
        print(e)
    else:
        run()
