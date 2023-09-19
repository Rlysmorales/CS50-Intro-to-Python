def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_len_valid(plate):
    if 2 <= len(plate) <= 6:
        print("Pass is_len", len(plate))
        return True
    else:
        print("NOT Pass is_len", len(plate))
        return False


def loop_all_character(plate):
    list_character = []
    list_plate = list(map(str, plate))
    count = 0
    for character in list_plate:
        if character not in ["!", "@", "#", "$", "%", "^", "&", "*", "()", "-", "+", "?", "_", "=", ",", "<", ">", "/",
                             ".",
                             " "]:
            list_character.append(character)
            count += 1
            print("Pass is_loop", character)

        else:
            print("NOT Pass is_loop", character)
            break

    if count == len(list(plate)):
        print("Pass is_count", count)
        return True
    else:
        print("Pass is_count", count)
        return False


def is_letters(plate):
    list_character = []
    list_plate = list(map(str, plate))
    count = 0
    for character in list_plate:
        list_character.append(character)
        count += 1
        print("Pass is_letter", character)

    if list_character[0].isalpha() and list_character[1].isalpha():
        print("pass is alpha", list_character)
        return True

    else:
        return False


def is_last_digit(plate):
    list_character = []
    list_plate = list(map(str, plate))
    count = 0
    for character in list_plate:
        list_character.append(character)
        count += 1
        print("Pass is_letter", character)

    if list_character[-1].isdigit():
        print("pass is digit", list_character)
        return True
    else:
        return False


def are_zero_first(character):
    first_zero = True
    for char in character:
        if not char.isalpha():
            if char == "0":
                print("Pass before key is zero", char, first_zero)
                first_zero = False
                print("Pass is zero", char, first_zero)
                break

            else:
                print("NOT before key Pass is zero", char, first_zero)
                first_zero = True
                print("NOT Pass is zero", char, first_zero)
                break

    return first_zero


def is_valid(plate):
    loop_valid = True
    while loop_valid:
        if not is_len_valid(plate):
            loop_valid = False
            break
        elif not loop_all_character(plate):
            loop_valid = False
            break
        elif not is_letters(plate):
            loop_valid = False
            break
        elif not is_last_digit(plate):
            loop_valid = False
            break
        elif not are_zero_first(plate):
            loop_valid = False
            break
        else:
            return True

    return loop_valid


main()
