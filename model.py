import sqlite3

def db_connect():
    con = sqlite3.connect("Tie-House.db")
    cur = con.cursor()
    print("Database connected")
    return con, cur
def exist(cur):
    res = cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='House' ''')
    #if the count is 1, then table exists
    if res.fetchone()[0]==1: 
        print('Table exists.')
        return True
    return False
    
def create_tables():
    cur, con = db_connect()
    if not exist(cur):
        cur.execute("""CREATE TABLE House(id INTEGER PRIMARY KEY,
                                        type VARCHAR(20)  NOT NULL,
                                        price INTEGER NOT NULL, 
                                        status VARCHAR(20) NOT NULL)""")
        cur.execute("""CREATE TABLE Seller(id INTEGER PRIMARY KEY,
                                           first_name VARCHAR(20) NOT NULL, 
                                           last_name VARCHAR(20) NOT NULL)""")
        cur.execute("""CREATE TABLE SoldHouse(id INTEGER PRIMARY KEY,
                                              house_id INTEGER, 
                                              seller_id INTEGER, 
                                              FOREIGN KEY(house_id) REFERENCES House(id),
                                              FOREIGN KEY(seller_id) REFERENCES Seller(id)
                                              )""")
        print("Tables created")
        res = cur.execute("SELECT name FROM sqlite_master")
        res.fetchone()
        print("Filling tables beep booop")
        fill_tables(cur)

    print("Printing tables")
    print_tables(cur)
    con.close()
    
def fill_tables(cur):
    cur.execute("""
    INSERT INTO House(type,price,status) VALUES
        ("Condo", 1000000,"Available"),
        ("Depa", 1500000,"Available"),
        ("Pantano", 500000,"Not Available")
    """)
    cur.execute("""
    INSERT INTO Seller(first_name,last_name) VALUES
        ("Emilio", "Rivas"),
        ("Alterbo", "Mutate"),
        ("Nahim", "Medellin")
    """)
    cur.execute("""
    INSERT INTO SoldHouse(house_id,seller_id) VALUES
        (3, 1)
    """)
    cur.commit()
def print_tables(cur):
    print("Printing table House")
    for row in cur.execute("Select * from House"):
        print(row)
    print("Printing table Seller")
    for row in cur.execute("Select * from Seller"):
        print(row)
    print("Printing table SoldHouse")
    for row in cur.execute("Select * from SoldHouse"):
        print(row)

