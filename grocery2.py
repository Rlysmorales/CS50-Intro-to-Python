def grocery_list():
    # Create empty list to store user input
    item_in_grocery_list = []
    # keep looping or accepting the user to enter item until CTRL-D
    while True:
        try:
            # prompt USer save input in upper case
            user_input = input("Item: ").upper().strip()
            # add user input to the list
            item_in_grocery_list.append(user_input)
            # Sort the item in a list use .sort() function
            item_in_grocery_list.sort()

        except EOFError:
            my_dic = {}
            for item in item_in_grocery_list:
                # add the repeating elements in the list
                if item in my_dic:
                    my_dic[item] += 1
                else:
                    my_dic[item] = 1
            for i in my_dic:
                # Display final list to the user after CTRL-D
                print(my_dic[i], i)
            break


grocery_list()

def grocery_list():
    # Create empty list to store user input
    my_dic = {}
    sorted_dict = dict(sorted(my_dic.items()))
    # keep looping or accepting the user to enter item until CTRL-D
    while True:

        try:
            # prompt USer save input in upper case
            user_input = input("Item: ").upper().strip()
            # add user input to the list

            if user_input in my_dic:
                my_dic[user_input] += 1
            else:
                my_dic[user_input] = 1


        except EOFError:
            sorted_dict = dict(sorted(my_dic.items()))
            for i in sorted_dict:
                # Display final list to the user after CTRL-D
                print(sorted_dict[i], i)
            break


grocery_list()
