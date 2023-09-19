def main():
    word = input("Input: ").strip()
    new_word = shorten(word)
    print(f"Output {new_word}")


def shorten(word):
    new_word = ""
    for letter in word:
        if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            pass
        else:
            new_word += letter

    return new_word


if __name__ == "__main__":
    main()
