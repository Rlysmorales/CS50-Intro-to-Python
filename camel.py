def naming_convention():
    user_input = input("camelCase: ")

    save_word = ""
    for answer in user_input:
        if answer.isupper():
            save_word += "_"
            save_word += answer.lower()
        else:
            save_word += answer
    print("snake_case: " + save_word)


naming_convention()
