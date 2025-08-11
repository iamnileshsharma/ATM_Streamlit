import sqlite3

def connect_db():
    con=sqlite3.connect("atm.db",check_same_thread=False)
    return con
def create_table():
    con=connect_db()
    cur=con.cursor()
    cur.execute('''create table if not exists users (
                id integer primary key autoincrement,
                username text unique,
                name text,
                password text,
                type text,
                balance real default 0
                )''')
    con.commit()
    cur.close()

