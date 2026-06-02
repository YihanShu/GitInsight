import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "gitinsight.db")


def get_conn():
    return sqlite3.connect(DB_PATH)