def main():
    greeting = input("Greeting: ").lower().strip()
    final_value = value(greeting)
    print(f"${final_value}")


def value(greeting):
    while True:

        if greeting.startswith("hello"):
            return 0
        elif greeting.startswith("h"):
            return 20
        else:
            return 100


if __name__ == "__main__":
    main()
