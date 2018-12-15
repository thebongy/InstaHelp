import sqlite3

def init_db():
    db = get_db()

    with open('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def get_db():
    db = sqlite3.connect(
        "./data.db",
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    db.row_factory = sqlite3.Row

    return db

init_db()
