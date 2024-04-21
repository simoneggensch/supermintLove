import sqlite3

def get_db_connection():
    conn = sqlite3.connect('sqLite/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
