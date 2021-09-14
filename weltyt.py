import sqlite3

def initializationDB(cursor):

        with open("TYTDB.sql") as base:
                for line in base:
                        cursor.execute(line)

lands_offert = {"humus": {"class": "humus", "id": 1, "growth_rate": 5, "price_ISL": 500, "plants": 0}, 
                "humus_sag": {"class": "humus_sag", "id": 2, "growth_rate": 4, "price_ISL": 400, "plants": 0}, 
                "brown_soil": {"class": "brown_soil", "id": 3, "growth_rate": 3, "price_ISL": 350, "plants": 0}, 
                "lessive_soil": {"class": "lessive_soil", "id": 4, "growth_rate": 2, "price_ISL": 250, "plants": 0},
                "clay_gravel": {"class": "clay_gravel", "id": 5, "growth_rate": 1, "price_ISL": 200, "plants": 0}}
#INSERT INTO lands VALUES ("humus", 1, 5, 500, 0)
print("Welcome to tyton")
conn = sqlite3.connect("TYTDB.db")

cur = conn.cursor()

initializationDB(cur)        

conn.commit()

for row in cur.execute('SELECT * FROM resources'):
        print(row)

for rows in cur.execute('SELECT * FROM lands'):
        print(rows)


buying_plants = input("To grow tobbaco you have to buy some plants. If you want do it, write \"Plants\" please. ")
if buying_plants == "Plants":
    amount = int(input("How many plants do you want to buy? Write only integer please. Overwise weltyt stops working. "))

    if type(amount) == int:
        money_amount = cur.execute('SELECT amount  FROM resources WHERE type = "Money" ').fetchone()[0]
        plants_price = cur.execute('SELECT price FROM resources WHERE type = "Plants" ').fetchone()[0]
        new_money_amount =  money_amount - amount * plants_price
        cur.execute(f'UPDATE resources SET amount = {new_money_amount}  WHERE type = "Money"; ') 

        plants_amount = cur.execute('SELECT amount  FROM resources WHERE type = "Plants" ').fetchone()[0]
        new_plants_amount = plants_amount + amount 
        cur.execute(f'UPDATE resources SET amount = {new_plants_amount}  WHERE type = "Plants"; ')     
    else:
        print("Invalid input")
# elif buing == "Lands":
#     print("What kind of lands do you want to buy?")
else:
    print("Invalid input")

buying_lands = input("If you want buy lands, write \"Lands\" please. ")
for Lands in buying_lands:

    if buying_lands == "Lands":
        show_me_lands = input("If you want see lands offert, write yes please. ")
        if show_me_lands == "yes":
            print(lands_offert)

        else:
            print("Go directly to buying ") 

            choose_class = input("What land class do you want to buy? Write only properly names of lands please. Overwise weltyt stops working. ")
            if choose_class == "humus" or "humus_sag" or "brown_soil" or "lessive_soil" or "clay_gravel":
                
                add_land = cur.execute(f'INSERT INTO lands VALUES ("{lands_offert[choose_class]["class"]}", {lands_offert[choose_class]["id"]}, {lands_offert[choose_class]["growth_rate"]}, {lands_offert[choose_class]["price_ISL"]}, {lands_offert[choose_class]["plants"]})')
                money_amount = cur.execute('SELECT amount  FROM resources WHERE type = "Money" ').fetchone()[0]
                lands_price = cur.execute(f'SELECT price FROM lands WHERE class = "{choose_class}" ').fetchone()[0]
                new_money_amount =  money_amount - lands_price
                cur.execute(f'UPDATE resources SET amount = {new_money_amount}  WHERE type = "Money"; ') 
                print(f"Buying {choose_class} is done properly ")

            else:
                print("Invalid input")
        buying_lands = input("If you want buy lands, write \"Lands\" please. ")    
        # elif choose_class == "humus_sag":
        #     add_humus_sag = cur.execute('INSERT INTO lands VALUES ("humus_sag", 2, 4, 400, 0)') 

        # elif choose_class == "brown_soil":
        #     add_brown_soil = cur.execute('INSERT INTO lands VALUES ("brown_soil", 3, 3, 350, 0)') 

        # elif choose_class == "lessive_soil":
        #     add_lessive_soil = cur.execute('INSERT INTO lands VALUES ("lessive_soil", 4, 2, 250, 0)')

        # elif choose_class == "clay_gravel":
        #     add_clay_gravel = cur.execute('INSERT INTO lands VALUES ("clay_gravel", 5, 1, 200, 0)') 
 


    # amount = int(input("How many plants do you want to buy? "))
    
    # money_amount = cur.execute('SELECT amount  FROM resources WHERE type = "Money" ').fetchone()[0]
    # plants_price = cur.execute('SELECT price FROM resources WHERE type = "Plants" ').fetchone()[0]
    # new_money_amount =  money_amount - amount * plants_price
    # cur.execute(f'UPDATE resources SET amount = {new_money_amount}  WHERE type = "Money"; ') 

    # plants_amount = cur.execute('SELECT amount  FROM resources WHERE type = "Plants" ').fetchone()[0]
    # new_plants_amount = plants_amount + amount 
    # cur.execute(f'UPDATE resources SET amount = {new_plants_amount}  WHERE type = "Plants"; ')     
    

    else:
        print("Shopping is finished ")

show_my_resources = input("If you want check your resources, write yes. ")
if show_my_resources == "yes":
        for row in cur.execute('SELECT * FROM resources'):
                print(row)

        for rows in cur.execute('SELECT * FROM lands'):
                print(rows)

else:
        print("Go forward")                

conn.close()