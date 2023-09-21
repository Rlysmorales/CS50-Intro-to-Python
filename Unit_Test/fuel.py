def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    final_result = gauge(percentage)
    print(final_result)


def convert(fraction):
    new_fraction = fraction.split("/")
    convert_true = True
    while convert_true:
        try:
            numerator_number, denominator_number = new_fraction

            get_decimal = int(numerator_number) / int(denominator_number)

            if get_decimal <= 1:
                percentage = round(get_decimal * 100)
                return percentage
            else:
                fraction = input("Fraction: ")

        except ZeroDivisionError:
            raise
        except ValueError:
            raise


def gauge(percentage):
    if 99 <= percentage <= 100:
        return "F"

    elif percentage <= 1:
        return "E"
    elif percentage > 100:
        main()
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()