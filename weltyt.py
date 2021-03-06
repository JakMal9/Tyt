import sqlite3


def initializationDB(cursor):

    with open("TYTDB.sql") as base:
        for line in base:
            cursor.execute(line)


def show_my_resources():
    for row in cur.execute("SELECT * FROM resources"):
        print(row)

    for rows in cur.execute("SELECT * FROM lands"):
        print(rows)


def get_resource_value(column, resource_type):
    return cur.execute(
        f'SELECT "{column}" FROM resources WHERE type = "{resource_type}";'
    ).fetchone()[0]


def update_resource_amount(amount, resource_type):

    cur.execute(
        f'UPDATE resources SET amount = {amount}  WHERE type = "{resource_type}";'
    )


def get_lands_value(column, land_id):
    return cur.execute(
        f'SELECT "{column}" FROM lands WHERE id = "{land_id}"'
    ).fetchone()[0]


def update_lands_plants(new_plants_in_lands, land_id):
    cur.execute(
        f'UPDATE lands SET plants = {new_plants_in_lands}  WHERE id = "{second_choice}";'
    )


def buy_plants(plants):
    amount = input("How many plants do you want to buy? Provide only integer please. ")

    try:
        amount = int(amount)

        money_amount = get_resource_value("amount", "Money")
        plants_price = get_resource_value("price", "Plants")

        new_money_amount = money_amount - amount * plants_price
        if new_money_amount < 0:
            print(errors["not_enough_money"])
            return

        update_resource_amount(new_money_amount, "Money")

        plants_amount = get_resource_value("amount", "Plants")

        new_plants_amount = plants_amount + amount
        update_resource_amount(new_plants_amount, "Plants")

        print("Well done plants deal. ")

    except ValueError:

        print(errors["only_integer"])


def buy_pesticides(pesticides):
    amount = input(
        "How many pesticides do you want to buy? Write only integer please. "
    )

    try:
        amount = int(amount)

        money_amount = get_resource_value("amount", "Money")
        pesticides_price = get_resource_value("price", "Pesticides")

        new_money_amount = money_amount - amount * pesticides_price
        if new_money_amount < 0:
            print(errors["not_enough_money"])
            return

        update_resource_amount(new_money_amount, "Money")

        pesticides_amount = get_resource_value("amount", "Pesticides")

        new_pesticides_amount = pesticides_amount + amount
        update_resource_amount(new_pesticides_amount, "Pesticides")

        print("Well done pesticides deal. ")

    except ValueError:
        print(errors["only_integer"])


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
            money_amount = cur.execute(
                'SELECT amount  FROM resources WHERE type = "Money";'
            ).fetchone()[0]

            lands_price = lands_offert[chosen_class]["price_ISL"]

            new_money_amount = money_amount - lands_price

            if new_money_amount < 0:
                print(errors["not_enough_money"])
                return

            cur.execute(
                f"INSERT INTO lands (class, growth_rate, price, plants, growth_percentage) VALUES "
                f'("{lands_offert[chosen_class]["class"]}", {lands_offert[chosen_class]["growth_rate"]},'
                f' {lands_offert[chosen_class]["price_ISL"]}, 0, 0);'
            )
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
    },
    "humus_sag": {
        "class": "humus_sag",
        "id": 2,
        "growth_rate": 4,
        "price_ISL": 400,
    },
    "brown_soil": {
        "class": "brown_soil",
        "id": 3,
        "growth_rate": 3,
        "price_ISL": 350,
    },
    "lessive_soil": {
        "class": "lessive_soil",
        "id": 4,
        "growth_rate": 2,
        "price_ISL": 250,
    },
    "clay_gravel": {
        "class": "clay_gravel",
        "id": 5,
        "growth_rate": 1,
        "price_ISL": 200,
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
    "pesticides": "Pesticides",
}

messages = {
    "first_choice": "Choose what would you like to do. If you want check your resources write "
    '"show_my_resources" please. If you want go directly to buying, write "buy". If you want avoid this step write "no" '
    " please.\n",
    "user_choice": 'To start grow tobbaco you need plants and lands. To buy plants write just "Plants", '
    'to buy lands write "Lands", to buy pesticides write "Pesticides" please.\n',
    "second_choice": "What land do you choose to plant? Provide proper id of your land."
    'To check your resources write "show_my_resources" To avoid this step, write "no" please.\n',
}

errors = {
    "only_integer": "Invalid input, write integer only please. ",
    "not_enough_money": "There is not enough money to finish this operation.",
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

turn_counting = 0
growing = 0
while True:
    turn_counting += 1
    print(f"Next turn number {turn_counting}")

    first_choice = input(messages["first_choice"])

    while True:

        if first_choice == commands["show_my_resources"]:
            show_my_resources()
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

    second_choice = input(messages["second_choice"])

    while True:

        if second_choice == "no":
            break
            print("Planting is finished.")

        elif second_choice == commands["show_my_resources"]:
            show_my_resources()
            second_choice = input(messages["second_choice"])

        else:

            try:
                plants_on_land = get_lands_value("plants", second_choice)

                if plants_on_land > 0:
                    print(
                        "You can plant only on empty land, choose another one please."
                    )

                else:
                    planting_amount = input(
                        "How many plants do you want to plant in your land?       "
                    )
                    planting_amount = int(planting_amount)

                    plants_in_lands = get_lands_value("plants", second_choice)

                    new_plants_in_lands = plants_in_lands + planting_amount

                    if new_plants_in_lands > 100:
                        print("On one land you can plant only 100 plants")

                    else:
                        update_lands_plants(new_plants_in_lands, second_choice)

                        plants_in_resources = get_resource_value("amount", "Plants")
                        new_plants_in_resources = plants_in_resources - planting_amount
                        if new_plants_in_resources < 0:
                            update_lands_plants(plants_in_lands, second_choice)

                            print(
                                "There is not enough plants to finish this operation."
                            )
                        else:
                            update_resource_amount(new_plants_in_resources, "Plants")

                            print(f"Well done planting in id {second_choice} land. ")

            except ValueError:
                print(errors["only_integer"])

            except TypeError:
                print("Invalid land input, provide id of your land, please.")

            second_choice = input(messages["second_choice"])

    print("Go forward")

    planted_lands = [p for p in cur.execute("SELECT * FROM lands WHERE plants>0")]

    for g in planted_lands:
        growing = g[5] + g[2] + 4
        cur.execute(
            f'UPDATE lands SET growth_percentage = {growing}  WHERE id = "{g[1]}";'
        )

    harvest = [
        grown
        for grown in cur.execute("SELECT * FROM lands WHERE growth_percentage>100")
    ]

    for h in harvest:
        update_resource_amount(
            get_resource_value("amount", "Tobbaco_good")
            + get_lands_value("plants", h[1]),
            "Tobbaco_good",
        )

        cur.execute(
            f'UPDATE lands SET growth_percentage = 0, plants = 0  WHERE id = "{h[1]}";'
        )

    get_out_of_game = input(
        'To get out of this game write "Go out", to go to next round write whatever. '
    )
    if get_resource_value("amount", "Money") > 10000:
        break
        print(f"You achieved success after {turn_counting} turns, game over!")
    elif get_out_of_game == "Go out":
        print(f"You did not achieve success after {turn_counting} turns.")
        break

    else:
        print("This turn is finished.")

conn.close()
