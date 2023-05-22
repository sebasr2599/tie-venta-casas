import sqlite3

def db_connect():
    con = sqlite3.connect("Tie-House.db")
    cur = con.cursor()
    print("Database connected")
    return con, cur

def create_tables():
    cur, con = db_connect()
    cur.execute("CREATE TABLE house(id, type, price, status)")
    cur.execute("CREATE TABLE SoldHouse(id, houseid, seller)")
    print("Tables created")
    res = cur.execute("SELECT name FROM sqlite_master")
    res.fetchone()