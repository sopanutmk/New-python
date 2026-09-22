import sqlite3

conn = sqlite3.connect('mydatabase.db')

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER HOT NULL,
        city TEET HOT NULL
        )
    ''')

cur.execute("INSERT INTO user (name, age,city)  VALUES ('Alice',25,'New York')")
cur.execute("INSERT INTO user (name, age,city)  VALUES ('Bob',20,'Old York')")
cur.execute("INSERT INTO user (name, age,city)  VALUES ('mix',18,'thai')")

conn.commit()

cur.execute("SELECT * FORM users WHERE age>28")
rows=cur.fetchall()

print("Users older than 28:")
for row in rows:
    print(f"ID: {row[0]},Name:{row[1]},Age: {row[2]},City:{row[3]}")

conn.close