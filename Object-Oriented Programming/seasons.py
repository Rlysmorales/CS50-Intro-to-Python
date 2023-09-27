import sys
from datetime import date
import inflect


def main():
    total_minutes = user_birthday_minutes(input("Date of Birthday: "))
    final_words = words_creation(total_minutes)
    print(final_words)


def user_birthday_minutes(user_birth):

    try:
        year, month, day = user_birth.split("-")
        int_year = int(year)
        int_month = int(month)
        int_day = int(day)

        start_datetime = date(int_year, int_month, int_day)

        today = date.today()
        subtract_time = today - start_datetime
        days_difference = subtract_time.days
        total_minutes = days_difference * 24 * 60
        print(total_minutes)
        return total_minutes

    except ValueError:
        sys.exit("Invalid date")


def words_creation(total_minutes):
    word_formation = inflect.engine()
    final_words = word_formation.number_to_words(total_minutes, andword="")
    final_sentence = final_words + " minutes"
    return final_sentence.capitalize()


if __name__ == "__main__":
    main()
