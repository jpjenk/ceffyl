import os
import random
import datetime
import time

import gpudb


def default_function():
    print('Holding pattern...')
    time.sleep(5000)


def insert_random(kml_api_base, db_conn_str, db_user, db_pass):

    sink_tbl_name = os.environ['SINK_TABLE']

    sink_tbl_scm = [
        ['time', 'string', 'datetime'],
        ['value', 'int', 'int8']
    ]

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
