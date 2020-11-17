import os
import random
import datetime
import time

import gpudb


def default_function(logger, kml_api_base, db_conn_str, db_user, db_pass):
    """Launch Ubuntu instance and pause."""

    pause = (
        int(os.environ.get('SLIP_PAUSE'))
        if os.environ.get('SLIP_PAUSE')
        else 3600
    )

    logger.info(f'KML API: {kml_api_base}')
    logger.info(f'Database: {db_conn_str}')
    logger.info(f'Holding pattern ({pause} sec) ...')
    time.sleep(pause)
    logger.info(f'Exiting now')


def insert_random(logger, kml_api_base, db_conn_str, db_user, db_pass):

    sink_tbl_name = os.environ['SINK_TABLE']
    logger.info(f'Inserting data into table: {sink_tbl_name}')

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
    logger.info(f'Connected to database: {db.host}')

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
    logger.info(f'Attached to table: {sink_tbl_hdl.name}')

    # Insert records
    logger.info('Begining insert .....')
    while True:
        record = {
            'time': datetime.datetime.utcnow().isoformat(' ')[:-3],
            'value': random.randint(10, 99)
        }
        logger.info(record)
        sink_tbl_hdl.insert_records([record])
        time.sleep(1)
