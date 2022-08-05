import sqlite3
from sqlite3 import Error
import os
from pprint import pprint


class BaseDBManager():

    def __init__(self, path, connect=True):
        self.path = path
        if connect == True:
            self.connect()

    def connect(self, path=False):
        self.connection = sqlite3.connect(self.path)

    def db_exists(self):
        if os.path.exists(self.path):
            return True
        else:
            return False

    def __del__(self):
        try:
            self.connection.close()
        except:
            return

    def create_table(self, sql):
        """ create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.connection.cursor()
            c.execute(sql)
        except sqlite3.Error as error:
            raise Exception("Error creating table, Message: " + error)

    def commit(self):
        self.connection.commit()

    def insert(self, query, values):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, values)
            self.commit()
            return cursor.lastrowid
        except sqlite3.Error as error:
            raise Exception("Error inserting, Message: " + error)

    def select(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.row_factory = sqlite3.Row
            cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as error:
            raise Exception("Error selecting, Message: " + error)
