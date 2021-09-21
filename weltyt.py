import sqlite3

def initializationDB(cursor):

        with open("TYTDB.sql") as base:
                for line in base:
                        cursor.execute(line)

def initializationDB(cursor):

    with open("TYTDB.sql") as base:
        for line in base:
            cursor.execute(line)

def show_my_resources(x):
    for row in cur.execute("SELECT * FROM resources"):
            print(row)

    for rows in cur.execute("SELECT * FROM lands"):
        print(rows)

def buy_plants(plants):
    amount = input(
                    "How many plants do you want to buy? Write only integer please. "
                )
            
    try:
        amount = int(amount)

        money_amount = cur.execute(
            'SELECT amount  FROM resources WHERE type = "Money";'
        ).fetchone()[0]
        plants_price = cur.execute(
            'SELECT price FROM resources WHERE type = "Plants";'
        ).fetchone()[0]
        new_money_amount = money_amount - amount * plants_price
        cur.execute(
            f'UPDATE resources SET amount = {new_money_amount}  WHERE type = "Money";'
        )
        plants_amount = cur.execute(
            'SELECT amount  FROM resources WHERE type = "Plants";'
        ).fetchone()[0]
        new_plants_amount = plants_amount + amount
        cur.execute(
            f'UPDATE resources SET amount = {new_plants_amount}  WHERE type = "Plants";'
        )
        print("Well done plants deal. ")
    except ValueError:
        
        print("Invalid input, write integer only please. ")

def buy_lands(lands):
    show_me_lands = input("If you want see lands offert, write yes please. \
        \
        ")
    if show_me_lands == "yes":
        print(lands_offert)

    else:
        print("Go directly to buying ")

        
        chosen_class = input(
            "What land class do you want to buy? Write only properly names of lands please. \
            \
            "
        )
    
        try: 
            
            add_land = cur.execute(
                f'INSERT INTO lands VALUES ("{lands_offert[choose_class]["class"]}", {lands_offert[choose_class]["id"]}, {lands_offert[choose_class]["growth_rate"]}, {lands_offert[choose_class]["price_ISL"]}, {lands_offert[choose_class]["plants"]});'
            )
            money_amount = cur.execute(
                'SELECT amount  FROM resources WHERE type = "Money";'
            ).fetchone()[0]
            lands_price = cur.execute(
                f'SELECT price FROM lands WHERE class = "{choose_class}";'
            ).fetchone()[0]
            new_money_amount = money_amount - lands_price
            cur.execute(
                f'UPDATE resources SET amount = {new_money_amount}  WHERE type = "Money";'
            )
        
            print(f"Buying {chosen_class} is done properly ")
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

first_choice = input("Choose what would you like to do. If you want check your resources write \"show_my_resources\" please. If you want go directly to buying, write \"buy\". If you want avoid this step write \"no\" please. \
    \
    ")
for choice in first_choice:


    if first_choice == "show_my_resources":
        show_my_resources(first_choice)
        first_choice = input("Choose what would you like to do. If you want check your resources write \"show_my_resources\" please. If you want go directly to buying, write \"buy\". If you want avoid this step write \"no\" please. \
            \
            ")

    elif first_choice == "buy":
        what_buy = input("To start grow tobbaco you need plants and lands. To buy plants write just \"Plants\", to buy lands write \"Lands\" please. \
            \
            ")
        if what_buy == "Plants":
            buy_plants(what_buy)
            first_choice = input("Choose what would you like to do. If you want check your resources write \"show_my_resources\" please. If you want go directly to buying, write \"buy\". If you want avoid this step write \"no\" please. \
                \
                ")

        elif what_buy == "Lands":
            buy_lands(what_buy)
            first_choice = input("Choose what would you like to do. If you want check your resources write \"show_my_resources\" please. If you want go directly to buying, write \"buy\". If you want avoid this step write \"no\" please. \
                \
                ")
                   
        elif what_buy == "no":
            print("Shopping is finished ")
            break


        else:
            print("Invalid input")
            first_choice = input("Choose what would you like to do. If you want check your resources write \"show_my_resources\" please. If you want go directly to buying, write \"buy\". If you want avoid this step write \"no\" please. \
                \
                ")



else:
    print("Invalid input")
    first_choice = input("Choose what would you like to do. If you want check your resources write \"show_my_resources\" please. If you want go directly to buying, write \"buy\". If you want avoid this step write \"no\" please. \
        \
        ")

print("Shopping is finished")
print("Go forward")

conn.close()
