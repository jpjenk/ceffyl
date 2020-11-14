#!/usr/bin/python3

import random
import datetime
import time
import os
import sys


def grab_or_die(env_var_key):
    """Retrieve environment variables."""

    if env_var_key not in os.environ:
        print(f'Could not find environment variable: {env_var_key} ')
        sys.exit(1)

    return os.environ[env_var_key]


if __name__ == "__main__":

    # Retrieve environment variables
    kml_api_base = grab_or_die('KML_CONN_STR')
    db_conn_str = grab_or_die('DB_CONN_STR')
    db_user = grab_or_die('DB_USER')
    db_pass = grab_or_die('DB_PASS')


    x = 1/0
