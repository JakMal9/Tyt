DROP TABLE IF EXISTS resources; 
CREATE TABLE IF NOT EXISTS resources (type text UNIQUE, amount integer, unit text, price integer);
INSERT INTO resources VALUES ('Money', 1000, 'ILS', 1);
INSERT INTO resources VALUES ('Tobbaco_bad', 0, 'grams', 2);
INSERT INTO resources VALUES ('Tobbaco_good', 0, 'grams', 5);
INSERT INTO resources VALUES ('Plants', 0, 'pieces', 1);
INSERT INTO resources VALUES ('Company_name', 1, 'input', 0);
INSERT INTO resources VALUES ('Pesticides', 0, 'pieces', 2);
DROP TABLE IF EXISTS lands;
CREATE TABLE IF NOT EXISTS lands (class text, id INTEGER PRIMARY KEY AUTOINCREMENT, growth_rate integer, price integer, plants integer);
