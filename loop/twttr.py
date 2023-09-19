def vowels():
    user_input = input("Input: ").strip()
    new_word = ""
    for letter in user_input:
        if letter in ["a", "e", "i", "o", "u"]:
            pass
        else:
            new_word += letter
    print("Output" + new_word)


vowels()
