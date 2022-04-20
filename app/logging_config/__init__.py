import logging
from logging.config import dictConfig

import flask
from flask import request, current_app

from app.logging_config.app_log_config import LOGGING_CONFIG

log_configuration = flask.Blueprint('log_configuration', __name__)


@log_configuration.before_app_request
def before_request_logging():
    current_app.logger.info("Application starting new request")
    log = logging.getLogger("request_logger")
    log.info("Processing request")
    log.debug(request)


@log_configuration.after_app_request
def after_request_logging(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response
    elif request.path.startswith('/bootstrap'):
        return response
    current_app.logger.info("Application processed request")

    log = logging.getLogger("request_logger")
    log.info("Request complete")
    log.debug(response)
    return response


@log_configuration.before_app_first_request
def configure_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
    log = logging.getLogger("app_logger")
    log.info("Log configuration complete")
    log = logging.getLogger("error_logger")
    log.info("Application errors will be logged here")
