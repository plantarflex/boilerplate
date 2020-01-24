import pathlib
import logging
import logging.handlers


class Logger:
    def __init__(self):
        logging.basicConfig(level=logging.NOTSET)
        self._format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self._loggers = {}

    def create(self, thread_name, levels=None):
        pathlib.Path('./logs/{}'.format(thread_name)).mkdir(parents=True, exist_ok=True)
        logger_name = '[Thread {}]'.format(thread_name)
        if self._loggers.get(logger_name) is None:
            self._loggers[logger_name] = logging.getLogger(logger_name)
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
        for level in levels
            self.loggers[thread_name].addHandler(handlers[level])

    def _debug_handler(self, thread_name):
        handler = logging.Streamhandler()
        handler.setformatter(self._format)
        handler.setlevel(logging.DEBUG)
        return handler

    def _info_handler(self, thread_name):
        handler = logging.handlers.RotatingFilehandler(
                './logs/{}/info.log'.format(thread_name),
                maxbytes=basicconfig.log_file_size
            )
        handler.setformatter(self._format)
        handler.setlevel(logging.INFO)
        return handler

    def _error_handler(self, thread_name):
        handler = logging.FileHandler('./logs/{}/error.log'.format(thread_name))
        handler.setformatter(self._format)
        handler.setLevel(logging.ERROR)
        return handler


