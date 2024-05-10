class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer.")
        if self.cookies + n > self.capacity:
            raise ValueError(
                "Adding that many cookies would exceed the cookie jar's capacity."
            )
        self.cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer.")
        if self.cookies - n < 0:
            raise ValueError("There aren't that many cookies in the cookie jar.")
        self.cookies -= n

    @property
    def size(self):
        return self.cookies


def main():
    jar = Jar()
    user_deposit = int(input())
    jar.deposit(user_deposit)
    user_withdraw = int(input())
    jar.withdraw(user_withdraw)
    print(jar)


if __name__ == "__main__":
    main()
