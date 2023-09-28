import os
from hangman_ascii import hangman
from welcome import welcome, lose, win
from wonderwords import RandomWord


def main():
    hangman_game = Hangman()
    if hangman_game.user_choice():
        chosen_word = hangman_game.choose_word()
        hangman_game.start_game(chosen_word)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_game_outcome(outcome, chosen_word):
    if outcome == "You Win":
        clear_screen()
        print(f" GREAT JOB!! The random word is: ' {chosen_word}'")
        print(win)

        return "You Win"

    elif outcome == "You Lose":
        clear_screen()
        print(f"Sorry but the random word is: ' {chosen_word}'")
        print(lose)
        return "You Lose"


class Hangman:
    def user_choice(self):
        print(welcome)

        while True:
            user_input = input("Do you wish to start a new game? Type 'yes' or 'no': ").lower().strip()
            if user_input == "yes":
                return True

            elif user_input == "no":
                clear_screen()
                print("Thank you for Playing!!!")
                break

            else:
                input("Do you wish to start a new game? Type 'yes' or 'no': ").lower().strip()

    def choose_word(self):
        clear_screen()
        random_words = RandomWord()
        chosen_word = random_words.word()
        return chosen_word

    def start_game(self, chosen_word):
        word_length = len(chosen_word)
        print(hangman[6])
        total_lives = 6
        print(f"You total lives is: {total_lives}")

        display = []
        for _ in range(word_length):
            display += "_"

        print(f"WORD DISPLAY: {' '.join(display)}")
        already_guess = []
        letter_not_word = []
        finished_game = False
        while not finished_game:

            guess = input("Guess a letter: ")
            clear_screen()
            print(f"Letters Not in Word: {' '.join(already_guess)}")
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
                letter_not_word.append(guess)
                total_lives -= 1
                if total_lives == 0:
                    clear_screen()
                    outcome = "You Lose"
                    display_game_outcome(outcome, chosen_word)
                    break

            print(f"WORD DISPLAY: {' '.join(display)}")
            print(f"Letters Already Used and Not in Word: {' '.join(letter_not_word)}")

            if "_" not in display:
                clear_screen()
                outcome = "You Win"
                display_game_outcome(outcome, chosen_word)
                break

            print(hangman[total_lives])


if __name__ == "__main__":
    main()
