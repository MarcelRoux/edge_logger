import sqlite3
from sqlite3 import Connection, Cursor
from typing import Tuple

from table_scripts import TEMPERATURE_TABLE
from time_module import now_datetime_hour_string

SENSOR = 'dht'
DB_ROOT = './data'


class SensorLog:

    def __init__(self, sensor=SENSOR, table_script=TEMPERATURE_TABLE, db_root=DB_ROOT):
        self.sensor = sensor
        self.db_root = db_root

        conn, cur = self.cursor()
        self.setup_table(table_script, conn, cur)

    def cursor(self) -> Tuple[Connection, Cursor]:
        '''
        Sets up a table connection and creates a file if none exists.
        '''
        db_name = f'{DB_ROOT}/{self.sensor}_{now_datetime_hour_string()}.db'

        conn = sqlite3.connect(db_name)
        cur = conn.cursor()

        return conn, cur

    def setup_table(self, table_script, conn, cur):
        '''
        Execute table creation script.
        '''
        cur.execute(table_script)
        conn.commit()
