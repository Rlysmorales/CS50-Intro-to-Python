def grocery_list():
    # Create empty list to store user input
    my_dic = {}

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
            for key, value in sorted_dict.items():
                # Display final list to the user after CTRL-D
                print(value, key)
            exit(0)


grocery_list()
