cur.execute('''CREATE TABLE resources
				(Types text, Amount integer, Unit text, Price integer)''')

cur.execute("INSERT INTO resources VALUES ('Money', 1000, 'ILS', 1)")
cur.execute("INSERT INTO resources VALUES ('Tobbaco_bad', 0, 'grams', 2)")
cur.execute("INSERT INTO resources VALUES ('Tobbaco_good', 0, 'grams', 5)")
cur.execute("INSERT INTO resources VALUES ('Plants', 0, 'pieces', 1)")
cur.execute("INSERT INTO resources VALUES ('Company_name', 1, 'input', 0)")
cur.execute("INSERT INTO resources VALUES ('Pesticides', 0, 'pieces', 2)")

cur.execute('''CREATE TABLE lands
				(Class text, ID numeric, Growth_rate integer, Price integer, Plants integer)''')
cur.execute("INSERT INTO lands VALUES ('humus', 1, 5, 500, 0)")
cur.execute("INSERT INTO lands VALUES ('humus_sag', 2, 4, 400, 0)")
cur.execute("INSERT INTO lands VALUES ('brown_soil', 3, 3, 350, 0)")
cur.execute("INSERT INTO lands VALUES ('lessive_soil', 4, 2, 250, 0)")
cur.execute("INSERT INTO lands VALUES ('clay_gravel', 5, 1, 200, 0)")

conn.commit()

for row in cur.execute('SELECT * FROM resources'):
        print(row)

for rows in cur.execute('SELECT * FROM lands'):
        print(rows)

