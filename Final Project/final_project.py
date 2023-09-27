import os
import sys
from hangman_ascii import hangman
from welcome import welcome, lose, win
import time
from wonderwords import RandomWord


def user_choice():
    print(welcome)

    while True:
        user_input = input("Do you wish to start a new game? Type 'yes' or 'no': ").lower().strip()
        if user_input == "yes":
            return True

        elif user_input == "no":
            clear_screen()
            sys.exit("Thank You for Playing!!!")

        else:
            input("Do you wish to start a new game? Type 'yes' or 'no': ").lower().strip()


def choose_word():
    clear_screen()
    random_words = RandomWord()
    chosen_word = random_words.word()
    return chosen_word


def start_game(chosen_word):
    word_length = len(chosen_word)
    print(hangman[6])
    total_lives = 6
    print(f"You total lives is: {total_lives}")

    display = []
    for _ in range(word_length):
        display += "_"

    print(f"WORD DISPLAY: {' '.join(display)}")

    already_guess = []
    finished_game = False
    while not finished_game:

        guess = input("Guess a letter: ").lower()
        clear_screen()
        if guess in already_guess:
            print(f"The word: ' {guess} ' has already been used")
        else:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    already_guess.append(guess)
                    display[position] = letter

        if guess not in chosen_word:
            print(f"Sorry, the word: ' {guess} ' is not in the random word")
            total_lives -= 1
            if total_lives == 0:
                finished_game = True
                outcome = "You Lose"
                display_game_outcome(outcome, chosen_word)

        print(f"WORD DISPLAY: {' '.join(display)}")
        if "_" not in display:
            finished_game = True
            outcome = "You Win"
            display_game_outcome(outcome, chosen_word)

        print(hangman[total_lives])


def display_game_outcome(outcome, chosen_word):
    if outcome == "You Win":
        clear_screen()
        print(f" GREAT JOB!! The random word is: ' {chosen_word}'")
        print(win)
        time.sleep(2)
        user_choice()

    elif outcome == "You Lose":
        clear_screen()
        print(f"Sorry but the random word is: ' {chosen_word}'")
        print(lose)
        time.sleep(2)
        user_choice()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    if user_choice():
        chosen_word = choose_word()
        start_game(chosen_word)


if __name__ == "__main__":
    main()
