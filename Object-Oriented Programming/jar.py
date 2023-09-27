class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):

        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("Too few cookies")

        if value > self.capacity:
            raise ValueError("Too many cookies")

        self._size = value


def main():
    jar = Jar()
    user_input = input("Do you want to deposit or withdraw: ")
    if user_input == "deposit":
        user_deposit = int(input("How many cookies are you depositing? "))
        if user_deposit < 0:
            raise ValueError
        jar.deposit(user_deposit)

    elif user_input == "withdraw":
        user_withdraw = int(input("How many cookies are you eating? "))
        if user_withdraw < 0:
            raise ValueError
        jar.withdraw(user_withdraw)

    print(jar)


if __name__ == "__main__":
    main()

