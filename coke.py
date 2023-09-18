def price_of_coke():
    coke_price = 50
    while coke_price > 0:
        print("Amount Due:", coke_price)
        user_input = int(input("Insert Coin: "))

        if user_input not in [5, 10, 25]:
            print("Amount Due:", coke_price)

        else:
            if user_input == 25:
                coke_price -= 25

            elif user_input == 10:
                coke_price -= 10

            elif user_input == 5:
                coke_price -= 5


    change_string = str(coke_price)
    change_owed = change_string.replace("-", "")
    print("Change Owed: " + change_owed)


price_of_coke()
