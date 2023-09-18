def ask_user(total=0):
    felipe_menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    try:
        user_item = input("Item: ").title().strip()
        total += felipe_menu[user_item]
        print(f"Total ${total:.2f}")
        ask_user(total)

    except KeyError:
        ask_user(total)

    except EOFError:
        exit(0)

ask_user()

