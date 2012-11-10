import sqlite3
from contextlib import closing

def connect_db(database):
    return sqlite3.connect(database)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()