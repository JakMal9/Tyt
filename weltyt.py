import sqlite3

def initializationDB(cursor):

        with open("TYTDB.sql") as base:
                for line in base:
                        cursor.execute(line)

print("Welcome to tyton")
conn = sqlite3.connect("TYTDB.db")

cur = conn.cursor()

initializationDB(cur)        

conn.commit()

for row in cur.execute('SELECT * FROM resources'):
        print(row)

for rows in cur.execute('SELECT * FROM lands'):
        print(rows)


buying_plants = input("Choose what do you want to buy? ")
if buying_plants == "Plants":
    amount = int(input("How many plants do you want to buy? "))
    
    money_amount = cur.execute('SELECT amount  FROM resources WHERE type = "Money" ').fetchone()[0]
    plants_price = cur.execute('SELECT price FROM resources WHERE type = "Plants" ').fetchone()[0]
    new_money_amount =  money_amount - amount * plants_price
    cur.execute(f'UPDATE resources SET amount = {new_money_amount}  WHERE type = "Money"; ') 

    plants_amount = cur.execute('SELECT amount  FROM resources WHERE type = "Plants" ').fetchone()[0]
    new_plants_amount = plants_amount + amount 
    cur.execute(f'UPDATE resources SET amount = {new_plants_amount}  WHERE type = "Plants"; ')     
    
# elif buing == "Lands":
#     print("What kind of lands do you want to buy?")
else:
    print("Invalid input")

buying_lands = input("Choose what do you want to buy? ")
if buying_lands == "Lands":
    show_me_lands = input("If you want see lands offert, write yes please. ")
    if show_me_lands == "yes":
        showing_lands = {"humus": {"growth_rate_5": "price_500_ISL"}, "humus_sag": {"growth_rate_4": "price_400_ISL"}, "brown_soil": {"growth_rate_3": "price_350_ISL"}, "lessive_soil": {"growth_rate_2": "price_250_ISL"}, "clay_gravel": {"growth_rate_1": "price_200_ISL"}}
        print(showing_lands)

        choose_class = input("What land class do you want to buy?")
        if choose_class == "humus":
            add_humus = cur.execute('INSERT INTO lands VALUES ("humus", 1, 5, 500, 0)')

        elif choose_class == "humus_sag":
            add_humus_sag = cur.execute('INSERT INTO lands VALUES ("humus_sag", 2, 4, 400, 0)') 

        elif choose_class == "brown_soil":
            add_brown_soil = cur.execute('INSERT INTO lands VALUES ("brown_soil", 3, 3, 350, 0)') 

        elif choose_class == "lessive_soil":
            add_lessive_soil = cur.execute('INSERT INTO lands VALUES ("lessive_soil", 4, 2, 250, 0)')

        elif choose_class == "clay_gravel":
            add_clay_gravel = cur.execute('INSERT INTO lands VALUES ("clay_gravel", 5, 1, 200, 0)') 

        else:
            print("Invalid input") 


    # amount = int(input("How many plants do you want to buy? "))
    
    # money_amount = cur.execute('SELECT amount  FROM resources WHERE type = "Money" ').fetchone()[0]
    # plants_price = cur.execute('SELECT price FROM resources WHERE type = "Plants" ').fetchone()[0]
    # new_money_amount =  money_amount - amount * plants_price
    # cur.execute(f'UPDATE resources SET amount = {new_money_amount}  WHERE type = "Money"; ') 

    # plants_amount = cur.execute('SELECT amount  FROM resources WHERE type = "Plants" ').fetchone()[0]
    # new_plants_amount = plants_amount + amount 
    # cur.execute(f'UPDATE resources SET amount = {new_plants_amount}  WHERE type = "Plants"; ')     
    

else:
    print("Invalid input")

show_my_resources = input("If you want check your resources, write yes. ")
if show_my_resources == "yes":
        for row in cur.execute('SELECT * FROM resources'):
                print(row)

        for rows in cur.execute('SELECT * FROM lands'):
                print(rows)

else:
        print("Go forward")                

conn.close()