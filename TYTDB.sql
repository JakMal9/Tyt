DROP TABLE IF EXISTS resources; 
CREATE TABLE IF NOT EXISTS resources (Type text UNIQUE, Amount integer, Unit text, Price integer);
INSERT INTO resources VALUES ('Money', 1000, 'ILS', 1);
INSERT INTO resources VALUES ('Tobbaco_bad', 0, 'grams', 2);
INSERT INTO resources VALUES ('Tobbaco_good', 0, 'grams', 5);
INSERT INTO resources VALUES ('Plants', 0, 'pieces', 1);
INSERT INTO resources VALUES ('Company_name', 1, 'input', 0);
INSERT INTO resources VALUES ('Pesticides', 0, 'pieces', 2);
CREATE TABLE IF NOT EXISTS lands (Class text, ID numeric, Growth_rate integer, Price integer, Plants integer);
