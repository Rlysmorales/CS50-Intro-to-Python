import random


def user_number_input():
    game_true = True
    while game_true:
        try:
            user_input = int(input("Level: "))
            random_number = random.randint(1, user_input)
            if user_input < 1:
                game_true = True
            elif random_number < 0:
                game_true = True
            else:
                user_guess_number(random_number, user_input)
                game_true = False

        except ValueError:
            user_number_input()

        except EOFError:
            exit(0)


def user_guess_number(random_number, user_input):
    guess_true = True
    while guess_true:
        try:
            guess_input = int(input("Guess: "))
            if guess_input < 1:
                guess_true = True
            elif guess_input > user_input:
                print("Too large!")
                guess_true = True
            elif guess_input < random_number:
                print("Too small!")
                guess_true = True
            elif guess_input > random_number:
                print("Too large!")
                guess_true = True
            elif guess_input == random_number:
                print("Just right!")
                guess_true = False

        except ValueError:
            user_guess_number(random_number, user_input)
        except EOFError:
            exit(0)

    print(random_number)
    print(user_input)


user_number_input()
