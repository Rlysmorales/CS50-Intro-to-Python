import inflect

def adieu():


    word_formation = inflect.engine()
    name_list = []
    input_true = True
    while input_true:
        try:
            user_input = input("Input: ").strip()
            name_list.append(user_input)
            mylist = word_formation.join(name_list)
        except EOFError:
            print("Adieu, adieu, to", mylist)
            exit(0)


adieu()