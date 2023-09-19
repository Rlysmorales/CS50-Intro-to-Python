def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(dollar):
    # TODO
    dollar = dollar.replace("$","")
    float_number = float(dollar)
    return float_number



def percent_to_float(percent):
    # TODO
    percent = percent.replace("%", "")
    float_percentage = float(percent)/100
    return float_percentage


main()