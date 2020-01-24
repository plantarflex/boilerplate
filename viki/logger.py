import pathlib
import logging
import logging.handlers

from config import Config

class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.NOTSET)
        self._format = logging.Formatter('%(asctime)s - [Thread %(name)s] - %(levelname)s - %(message)s')
        self._loggers = {}

    def create(self, thread_name, levels=None):
        pathlib.Path('./logs/{}'.format(thread_name)).mkdir(parents=True, exist_ok=True)
        if type(thread_name) is not str:
            print('thread name should be string type')
            raise ValueError
        if self._loggers.get(thread_name) is None:
            self._loggers[thread_name] = logging.getLogger(thread_name)
            self._attach_handlers(thread_name, levels)

    def __getitem__(self, thread_name):
        return self._loggers[thread_name]

    def __delitem__(self, thread_name):
        del self._loggers[thread_name]

    def _attach_handlers(self, thread_name, levels):
        handlers = {
            'DEBUG': self._debug_handler,
            'INFO': self._info_handler,
            'ERROR': self._error_handler
            }
        if levels is None or len(levels) == 0:
            levels = ['DEBUG']
        for level in levels:
            self._loggers[thread_name].addHandler(handlers[level](thread_name))

    def _debug_handler(self, thread_name):
        handler = logging.StreamHandler()
        handler.setFormatter(self._format)
        handler.setLevel(logging.DEBUG)
        return handler

    def _info_handler(self, thread_name):
       handler = logging.handlers.RotatingFileHandler(
           './logs/{}/info.log'.format(thread_name),
           maxBytes=Config.LOG_FILE_SIZE
           )
       handler.setFormatter(self._format)
       handler.setLevel(logging.INFO)
       return handler

    def _error_handler(self, thread_name):
        handler = logging.FileHandler('./logs/{}/error.log'.format(thread_name))
        handler.setFormatter(self._format)
        handler.setLevel(logging.ERROR)
        return handler


