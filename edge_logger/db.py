import os
import sqlite3
from sqlite3 import Connection, Cursor
from typing import Tuple

from time_module import now_datetime_hour_string, now_utc

SENSOR = 'sensor'
DB_ROOT = './data'


class SensorLog:

    def __init__(self,
                 sensor=SENSOR,
                 db_root=DB_ROOT):
        self.sensor = sensor
        self.db_root = db_root
        self.db_dir = self.setup_folder_structure()
        self.db_name = self.create_db_name()

    def __enter__(self):
        self.conn, self.cur = self.cursor()

        return self.conn

    def __exit__(self, type, value, traceback):
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
        '''
        Method that constructs time-split directories per sensor.
        '''
        now = now_utc()
        db_dir = f'{DB_ROOT}/{self.sensor}/{now.year}/{now.month}/{now.day}'

        os.makedirs(db_dir, exist_ok=True)

        return db_dir

    def _insert(self, data):
        '''
        Method that inserts values into table.
        '''
        fields = ','.join(data.keys())
        values = ','.join(map(str, data.values()))
        query = f'INSERT INTO {self.sensor} ({fields}) VALUES ({values})'

        self.cur.execute(query)

    def insert(self, data):
        '''
        Method to simplify interface for inserting table values.
        '''
        with self as conn:
            self.create_table(conn, data)
            self._insert(data)
