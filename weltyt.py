import sqlite3


def initializationDB(cursor):

    with open("TYTDB.sql") as base:
        for line in base:
            cursor.execute(line)

def show_my_resources(x):
    for row in cur.execute("SELECT * FROM resources"):
            print(row)

    for rows in cur.execute("SELECT * FROM lands"):
        print(rows)

def buing_plants(x):
    amount = input(
                    "How many plants do you want to buy? Write only integer please. "
                )
            
    try:
        amount = int(amount)

        money_amount = cur.execute(
            'SELECT amount  FROM resources WHERE type = "Money" '
        ).fetchone()[0]
        plants_price = cur.execute(
            'SELECT price FROM resources WHERE type = "Plants" '
        ).fetchone()[0]
        new_money_amount = money_amount - amount * plants_price
        cur.execute(
            f'UPDATE resources SET amount = {new_money_amount}  WHERE type = "Money"; '
        )
        plants_amount = cur.execute(
            'SELECT amount  FROM resources WHERE type = "Plants" '
        ).fetchone()[0]
        new_plants_amount = plants_amount + amount
        cur.execute(
            f'UPDATE resources SET amount = {new_plants_amount}  WHERE type = "Plants"; '
        )
        print("Buying plants was done properly. ")
    except ValueError:
        
        print("Invalid input, to buy any plant you have to write number as integer please. ")

def buying_lands(x):
    show_me_lands = input("If you want see lands offert, write yes please. ")
    if show_me_lands == "yes":
        print(lands_offert)

    else:
        print("Go directly to buying ")

        
        choose_class = input(
            "What land class do you want to buy? Write only properly names of lands please. "
        )
    
        try: 
            
            add_land = cur.execute(
                f'INSERT INTO lands VALUES ("{lands_offert[choose_class]["class"]}", {lands_offert[choose_class]["id"]}, {lands_offert[choose_class]["growth_rate"]}, {lands_offert[choose_class]["price_ISL"]}, {lands_offert[choose_class]["plants"]})'
            )
            money_amount = cur.execute(
                'SELECT amount  FROM resources WHERE type = "Money" '
            ).fetchone()[0]
            lands_price = cur.execute(
                f'SELECT price FROM lands WHERE class = "{choose_class}" '
            ).fetchone()[0]
            new_money_amount = money_amount - lands_price
            cur.execute(
                f'UPDATE resources SET amount = {new_money_amount}  WHERE type = "Money"; '
            )
        
            print(f"Buying {choose_class} is done properly ")
        except KeyError:
            print("Invalid input")



lands_offert = {
    "humus": {
        "class": "humus",
        "id": 1,
        "growth_rate": 5,
        "price_ISL": 500,
        "plants": 0,
    },
    "humus_sag": {
        "class": "humus_sag",
        "id": 2,
        "growth_rate": 4,
        "price_ISL": 400,
        "plants": 0,
    },
    "brown_soil": {
        "class": "brown_soil",
        "id": 3,
        "growth_rate": 3,
        "price_ISL": 350,
        "plants": 0,
    },
    "lessive_soil": {
        "class": "lessive_soil",
        "id": 4,
        "growth_rate": 2,
        "price_ISL": 250,
        "plants": 0,
    },
    "clay_gravel": {
        "class": "clay_gravel",
        "id": 5,
        "growth_rate": 1,
        "price_ISL": 200,
        "plants": 0,
    },
}

print("Welcome to tyton")
conn = sqlite3.connect("TYTDB.db")

cur = conn.cursor()

initializationDB(cur)

conn.commit()

first_choice = input("Choose what would you like to do. If you want check your resources write \"show_my_resources\" please. If you want go directly to buying, write \"buy\". if you want avoid this step write no please. ")
for x in first_choice:


    if first_choice == "show_my_resources":
        show_my_resources(first_choice)
        first_choice = input("Choose what would you like to do. If you want check your resources write \"show_my_resources\" please. If you want go directly to buying, write \"buy\" please. ")

    elif first_choice == "buy":
        what_buy = input("To start grow tobbaco you need plants and lands. To buy plants write just \"Plants\", to buy lands write \"Lands\" please. ")
        if what_buy == "Plants":
            buing_plants(what_buy)
            first_choice = input("Choose what would you like to do. If you want check your resources write \"show_my_resources\" please. If you want go directly to buying, write \"buy\" please. ")

        elif what_buy == "Lands":
            buying_lands(what_buy)
            first_choice = input("Choose what would you like to do. If you want check your resources write \"show_my_resources\" please. If you want go directly to buying, write \"buy\" please. ")
                   
        elif what_buy == "no":
            print("Shopping is finished ")
            break


        else:
            print("Invalid input")
            



else:
    print("Shopping is finished ")
    print("Go forward")


    #if buying_lands == "Lands":
        
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

    #else:
       # print("Shopping is finished ")

conn.close()
