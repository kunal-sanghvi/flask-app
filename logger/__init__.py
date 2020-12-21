from json_log_formatter import JSONFormatter
from logging import INFO, RootLogger, StreamHandler


class StdoutLogger(object):

    def __init__(self, log_level=INFO):
        hdlr = StreamHandler()
        hdlr.setLevel(log_level)
        hdlr.setFormatter(JSONFormatter)
        self._logger = RootLogger(log_level)
        self._logger.addHandler(hdlr=hdlr)

    def debug(self, msg, extra=None):
        extra = {} if not extra else extra
        self._logger.debug(msg, extra=extra)

    def info(self, msg, extra=None):
        extra = {} if not extra else extra
        self._logger.info(msg, extra=extra)

    def warning(self, msg, extra=None):
        extra = {} if not extra else extra
        self._logger.warning(msg, extra=extra)

    def error(self, msg, extra=None):
        extra = {} if not extra else extra
        self._logger.error(msg, extra=extra)

    def fatal(self, msg, extra=None):
        extra = {} if not extra else extra
        self._logger.fatal(msg, extra=extra)
