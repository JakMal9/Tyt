import sqlite3


print("Welcome to tyton")
conn = sqlite3.connect("TYTDB.db")

cur = conn.cursor()

def my_function(base):
        for line in base:
                cur.execute(line)

first_tables = open("TYTDB.sql")

my_function(first_tables)        


conn.commit()

for row in cur.execute('SELECT * FROM resources'):
        print(row)

for rows in cur.execute('SELECT * FROM lands'):
        print(rows)

conn.close()
