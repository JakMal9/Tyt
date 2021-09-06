import sqlite3


print("Welcome to tyton")
conn = sqlite3.connect("TYTDB.db")

cur = conn.cursor()
base = open("TYTDB.sql")

for line in base:
        cur.execute(line)



conn.commit()

for row in cur.execute('SELECT * FROM resources'):
        print(row)

for rows in cur.execute('SELECT * FROM lands'):
        print(rows)

conn.close()
