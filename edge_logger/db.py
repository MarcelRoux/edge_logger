import sqlite3
import os
from sqlite3 import Connection, Cursor
from typing import Tuple

from table_scripts import SENSOR_TABLE_CREATE
from time_module import now_utc, now_datetime_hour_string

SENSOR = 'sensor'
DB_ROOT = './data'


class SensorLog:

    def __init__(self,
                 sensor=SENSOR,
                 table_create_script=SENSOR_TABLE_CREATE,
                 db_root=DB_ROOT):
        print('__init__ called')
        self.sensor = sensor
        self.db_root = db_root
        self.table_create_script = table_create_script

        self.db_dir = self.setup_folder_structure()
        self.db_name = self.create_db_name()

    def __enter__(self):
        print('__enter__ called')
        self.conn, self.cur = self.cursor()
        # self.create_table()

        return self.conn

    def __exit__(self, type, value, traceback):
        print('__exit__ called')
        self.conn.commit()
        self.conn.close()

    def create_db_name(self):
        '''
        Sets up a database file name.
        '''
        return f'{self.db_dir}/{self.sensor}_{now_datetime_hour_string()}.db'

    def cursor(self, db_name=None) -> Tuple[Connection, Cursor]:
        '''
        Sets up a table connection and creates a file if none exists.
        '''
        if(db_name is None):
            db_name = self.db_name

        conn = sqlite3.connect(db_name)
        cur = conn.cursor()

        return conn, cur

    def create_table(self):
        '''
        Execute table creation script.
        '''
        self.cur.execute(self.table_create_script)
        # self.conn.commit()

    def setup_folder_structure(self):
        now = now_utc()
        db_dir = f'{DB_ROOT}/{self.sensor}/{now.year}/{now.month}/{now.day}'

        os.makedirs(db_dir, exist_ok=True)

        return db_dir

    def insert(self, values):
        insert_values = ','.join(map(str, values))
        query = f'{self.table_insert_script}({insert_values})'

        self.cur.execute(query)
        self.conn.commit()
