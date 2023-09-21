def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if not 2 <= len(plate) <= 6:
        return False
    counter = 1
    if_is_digit = False
    for character in plate:
        if counter <= 2:
            if not character.isalpha():
                return False
        else:
            if not if_is_digit:
                if not character.isalpha() and not character.isdigit():
                    return False
                elif character == "0":
                    return False

                elif character.isdigit():
                    if_is_digit = True

            else:
                if not character.isdigit():
                    return False

        counter += 1

    return True


if __name__ == "__main__":
    main()
