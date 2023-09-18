def fruit_nutrition():
    user_input = input("Item: ").lower().strip()

    dic_fruits = {"apple": '130', "avocado": '50', "banana": '110', "cantaloupe": '50', "grapefruit": '60',
                  "grapes": '90', "honeydew melon": '130', "kiwifruit": '90', "lemon": '15', "lime": '20',
                  "nectarine": '60', "orange": '80', "peach": '60', "pear": '100', "pineapple": '50', "plums": '70',
                  "strawberries": '50', "sweet cherries": '100', "tangerine": '50', "Watermelon": '80'}

    for fruit in dic_fruits:
        if user_input == fruit:
            print("Calories:", dic_fruits[fruit])


fruit_nutrition()
