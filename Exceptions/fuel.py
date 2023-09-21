def fuel_int():
    fuel_true = True
    while fuel_true:
        try:
            numerator_number, denominator_number = input("Fraction: ").split("/")
            get_decimal = int(numerator_number) / int(denominator_number)
            get_percent = round(get_decimal * 100)

            if 99 <= get_percent <= 100:
                print("F")
                fuel_true = False
            elif get_percent <= 1:
                print("E")
                fuel_true = False
            elif get_percent > 100:
                fuel_true = True
            else:
                print(get_percent, "%", sep='')
                fuel_true = False
        except ZeroDivisionError:
            ...
        except ValueError:
            ...


fuel_int()
