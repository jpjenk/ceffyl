#!/usr/bin/python3

import time
import os
import sys
import logging

def create_logger(logname):
    """Instantiate logging module."""

    logger = logging.getLogger(logname)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    if (logger.hasHandlers()):
        logger.handlers.clear()
    logger.addHandler(handler)

    return logger


def grab_or_die(env_var_key):
    """Retrieve environment variables."""

    if env_var_key not in os.environ:
        print(f'Could not find environment variable: {env_var_key} ')
        sys.exit(1)

    return os.environ[env_var_key]


def get_launch():
    if 'SLIP_MODULE' in os.environ and 'SLIP_FUNCTION' in os.environ:
        return os.environ['SLIP_MODULE'], os.environ['SLIP_FUNCTION']
    else:
        return 'demo', 'default_function'


if __name__ == "__main__":

    # Instantiate logger
    logger = create_logger('slipway')

    # Retrieve environment variables
    kml_api_base = grab_or_die('KML_CONN_STR')
    db_conn_str = grab_or_die('DB_CONN_STR')
    db_user = grab_or_die('DB_USER')
    db_pass = grab_or_die('DB_PASS')
    logger.info('================')
    logger.info(f'KML: {kml_api_base}')
    logger.info(f'DB: {db_conn_str}')
    logger.info(f'User: {db_user}')
    if db_pass:
        logger.info('Password: ********')
    else:
        logger.info('Password:')

    # Get module and function names if available
    module, function = get_launch()

    # Assign and call function
    run_func = getattr(__import__(module), function)
    logger.info(f'Starting: {module}::{function}')
    logger.info('================')
    run_func(logger, kml_api_base, db_conn_str, db_user, db_pass)
