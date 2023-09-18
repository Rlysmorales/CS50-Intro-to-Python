import random
import sys


def main():
    get_level()


def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                user_addition(level)
                sys.exit(0)
            else:
                get_level()
        except ValueError:
            get_level()


def generate_integer(level):
    print("In the generate func", level)
    if level == 1:
        left_number = random.randint(0, 9)
        right_number = random.randint(0, 9)
        return left_number, right_number
    elif level == 2:
        left_number = random.randint(10, 99)
        right_number = random.randint(10, 99)
        return left_number, right_number
    elif level == 3:
        left_number = random.randint(100, 999)
        right_number = random.randint(100, 999)

        return left_number, right_number


def user_addition(level):
    left_number, right_number = generate_integer(level)
    count_right_answers = 0
    total_question = 10

    still_adding = True
    wrong_addition = 1
    while still_adding:
        print(total_question)
        if total_question <= 0:
            print("Score:", count_right_answers)
            exit(0)
        else:
            total_question -= 1

        try:
            addition = left_number + right_number
            user_answer = int(input(f"{left_number} + {right_number} = "))
            if user_answer == addition:
                count_right_answers += 1
                left_number, right_number = generate_integer(level)
                still_adding = True

            elif user_answer != addition:
                if wrong_addition <= 3:
                    print("EEE")
                    wrong_addition += 1
                    still_adding = True
                else:
                    print("Score:", count_right_answers)
                    break

        except ValueError:
            still_adding = True


if __name__ == "__main__":
    main()

# promt user for a level which are 1, 2, 3
# Randomley generate ten problems. Maybe create a counter.
# Generate a counter that everytime the user get an answer wrong it will subtract from the 10. Display score at end
# if User get answer wrong display EEE. If user get three consecutive EEE end game. If not reset EEE.


# :) professor.py exists
# :) Little Professor rejects level of 0
# :) Little Professor rejects level of 4
# :) Little Professor rejects level of "one"
# :( Little Professor accepts valid level
#     timed out while waiting for program to exit
# :| At Level 1, Little Professor generates addition problems using 0–9
#     can't check until a frown turns upside down
# :| At Level 2, Little Professor generates addition problems using 10–99
#     can't check until a frown turns upside down
# :| At Level 3, Little Professor generates addition problems using 100–999
#     can't check until a frown turns upside down
# :| Little Professor generates 10 problems before exiting
#     can't check until a frown turns upside down
# :| Little Professor displays number of problems correct
#     can't check until a frown turns upside down
# :| Little Professor displays EEE when answer is incorrect
#     can't check until a frown turns upside down
# :| Little Professor shows solution after 3 incorrect attempts
#     can't check until a frown turns upside down