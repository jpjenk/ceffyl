#!/usr/bin/python3

import random
import datetime
import time
import os
import sys

import gpudb

sink_tbl_scm = [
    ['time', 'string', 'datetime'],
    ['value', 'int', 'int8']
]


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
    sink_tbl_name = grab_or_die('SINK_TABLE')

    # Get database handle
    db = gpudb.GPUdb(
        host=db_conn_str,
        username=db_user,
        password=db_pass
    )

    # Create table if not existing
    if db.has_table(sink_tbl_name)['table_exists']:
        sink_tbl_hdl = gpudb.GPUdbTable(
            name=sink_tbl_name,
            db=db
        )
    else:
        sink_tbl_hdl = gpudb.GPUdbTable(
            _type=sink_tbl_scm,
            name=sink_tbl_name,
            db=db
        )

    # Insert records
    while True:
        sink_tbl_hdl.insert_records([{
            'time': datetime.datetime.utcnow().isoformat(' ')[:-3],
            'value': random.randint(10, 99)
        }])
        time.sleep(1)
