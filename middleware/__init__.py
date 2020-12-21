import uuid

from config import API_USER_NAME, API_USER_PASS, LOG_LEVEL
from flask import request, Response
from logger import StdoutLogger


basic_logger = StdoutLogger(LOG_LEVEL)


class LoggingMiddleware(object):

    def __init__(self, logger: StdoutLogger, api_method, api_path, **kwargs):
        self.logger = logger
        self.extra = {
            'api_id': uuid.uuid4(),
            'api_method': api_method,
            'api_path': api_path
        }
        if kwargs:
            self.extra.update(kwargs)

    def debug(self, msg):
        self.logger.debug(msg, extra=self.extra)

    def info(self, msg):
        self.logger.info(msg, extra=self.extra)

    def warning(self, msg):
        self.logger.warning(msg, extra=self.extra)

    def error(self, msg):
        self.logger.error(msg, extra=self.extra)

    def fatal(self, msg):
        self.logger.fatal(msg, extra=self.extra)


def require_authenticate():
    return Response('login with proper credentials', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


def basic_auth(func):
    def wrapper(rest_handler, *args, **kwargs):
        auth = request.authorization
        if auth:
            if auth.username == API_USER_NAME and auth.password == API_USER_PASS:
                rest_handler.log = LoggingMiddleware(logger=basic_logger,
                                                     api_method=request.method,
                                                     api_path=request.path)
                return func(rest_handler, *args, **kwargs)
        require_authenticate()
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper