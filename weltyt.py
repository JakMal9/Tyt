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

def get_resource(column, resource_type):
        return cur.execute(
        f'SELECT "{column}" FROM resources WHERE type = "{resource_type}";'
    ).fetchone()[0]



def update_resource(amount, resource_type):
    cur.execute(
        f'UPDATE resources SET amount = {amount}  WHERE type = "{resource_type}";'
    )



def buy_plants(plants):
    amount = input("How many plants do you want to buy? Provide only integer please. ")

    try:
        amount = int(amount)

        money_amount = get_resource("amount", "Money")
        plants_price = get_resource("price", "Plants")
            
        new_money_amount = money_amount - amount * plants_price
        update_resource(new_money_amount, "Money")
        
        plants_amount = get_resource("amount", "Plants")
        
        new_plants_amount = plants_amount + amount
        update_resource(new_plants_amount, "Plants")
    
        print("Well done plants deal. ")
    except ValueError:

        print("Invalid input, provide integer only please. ")


def buy_pesticides(pesticides):
    amount = input("How many pesticides do you want to buy? Write only integer please. ")

    try:
        amount = int(amount)

        money_amount = get_resource("amount", "Money")
        pesticides_price = get_resource("price", "Pesticides")
            
        new_money_amount = money_amount - amount * pesticides_price
        update_resource(new_money_amount, "Money")
            
        pesticides_amount = get_resource("amount", "Pesticides")
        
        new_pesticides_amount = pesticides_amount + amount
        update_resource(new_pesticides_amount, "Pesticides")
     
        print("Well done pesticides deal. ")
    except ValueError:

        print("Invalid input, write integer only please. ")


def buy_lands(lands):
    show_me_lands = input(
        "If you want see lands offert, write yes please. \
        \
        "
    )
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
                f'INSERT INTO lands VALUES ("{lands_offert[chosen_class]["class"]}", {lands_offert[chosen_class]["id"]}, {lands_offert[chosen_class]["growth_rate"]}, {lands_offert[chosen_class]["price_ISL"]}, {lands_offert[chosen_class]["plants"]});'
            )
            money_amount = cur.execute(
                'SELECT amount  FROM resources WHERE type = "Money";'
            ).fetchone()[0]
            lands_price = cur.execute(
                f'SELECT price FROM lands WHERE class = "{chosen_class}";'
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

explanation = {
    "Help": "Explain all commands",
    "show_my_resources": "Shows you what resources you have exactly in this " "time.",
    "buy": "shows what is possible to buy in this round.",
    "Plants": "Opens posibility of buying plants.",
    "Lands": "Opens posibility of buying lands.",
}

commands = {
    "help": "Help",
    "show_my_resources": "show_my_resources",
    "buy": "buy",
    "plants": "Plants",
    "lands": "Lands",
    "pesticides": "Pesticides"
}

messages = {
    "first_choice": "Choose what would you like to do. If you want check your resources write "
    '"show_my_resources" please. If you want go directly to buying, write "buy". If you want avoid this step write "no" '
    " please.\n",
    "user_choice": 'To start grow tobbaco you need plants and lands. To buy plants write just "Plants", '
    'to buy lands write "Lands", to buy pesticides write "Pesticides" please.\n',
}

print(explanation.keys())

print("Welcome to tyton")
print(
    'In every input if you write "Help", you will see explanation of all options which you can use.'
)
conn = sqlite3.connect("TYTDB.db")

cur = conn.cursor()

initializationDB(cur)

conn.commit()

first_choice = input(messages["first_choice"])


while True:

    if first_choice == commands["show_my_resources"]:
        show_my_resources(first_choice)
        first_choice = input(messages["first_choice"])

    elif first_choice == commands["buy"]:
        user_choice = input(messages["user_choice"])

        if user_choice == commands["plants"]:
            buy_plants(user_choice)
            first_choice = input(messages["first_choice"])

        elif user_choice == commands["lands"]:
            buy_lands(user_choice)
            first_choice = input(messages["first_choice"])

        elif user_choice == commands["pesticides"]:
            buy_pesticides(user_choice)
            first_choice = input(messages["first_choice"])

        elif user_choice == commands["help"]:
            print(explanation)
            user_choice = input(messages["user_choice"])

        else:
            print("Invalid input")
            first_choice = input(messages["first_choice"])

    elif first_choice == commands["help"]:
        print(explanation)
        first_choice = input(messages["first_choice"])

    elif first_choice == "no":
        print("Shopping is finished ")
        break

    else:
        print("Invalid input")
        first_choice = input(messages["first_choice"])

print("Go forward")

conn.close()
