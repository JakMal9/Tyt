import sqlite3


print("Welcome to tyton")
conn = sqlite3.connect("TYTDB.db")

cur = conn.cursor()

def initializationDB(cursor):

        with open("TYTDB.sql") as base:
                for line in base:
                        cursor.execute(line)

initializationDB(cur)        

conn.commit()

for row in cur.execute('SELECT * FROM resources'):
        print(row)

for rows in cur.execute('SELECT * FROM lands'):
        print(rows)

conn.close()
