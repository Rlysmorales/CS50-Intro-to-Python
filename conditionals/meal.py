def main():
    convert(input("What time is it? "))


def convert(time):
    hour, minutes = time.split(":")

    hour_float = float(hour)
    minutes_float = float(minutes)
    new_math = hour_float + (minutes_float * 1 / 60)

    if 7.0 <= new_math <= 8.0:
        print("breakfast time")
    elif 12.00 <= new_math <= 13.0:
        print("lunch time")
    elif 18.00 <= new_math <= 19.0:
        print("dinner time")

    return new_math


if __name__ == "__main__":
    main()
