import sqlite3
import os
from sqlite3 import Connection, Cursor
from typing import Tuple

from table_scripts import TEMPERATURE_TABLE_CREATE, TEMPERATURE_TABLE_INSERT
from time_module import now_utc, now_datetime_hour_string

SENSOR = 'dht'
DB_ROOT = './data'


class SensorLog:

    def __init__(self, sensor=SENSOR,
                 table_setup_script=TEMPERATURE_TABLE_CREATE,
                 table_insert_script=TEMPERATURE_TABLE_INSERT, db_root=DB_ROOT):
        self.sensor = sensor
        self.db_root = db_root
        self.table_insert_script = table_insert_script

        self.db_dir = self.setup_folder_structure()
        self.conn, self.cur = self.cursor()
        self.setup_table(table_setup_script)

    def cursor(self) -> Tuple[Connection, Cursor]:
        '''
        Sets up a table connection and creates a file if none exists.
        '''
        db_name = f'{self.db_dir}/{self.sensor}_{now_datetime_hour_string()}.db'

        conn = sqlite3.connect(db_name)
        cur = conn.cursor()

        return conn, cur

    def setup_table(self, table_script):
        '''
        Execute table creation script.
        '''
        self.cur.execute(table_script)
        self.conn.commit()

    def setup_folder_structure(self):
        now = now_utc()
        db_dir = f'{DB_ROOT}/{self.sensor}/{now.year}/{now.month}/{now.day}'

        os.makedirs(db_dir, exist_ok=True)

        return db_dir

