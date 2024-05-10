class jar:
    def __init__(self, capacity=12):
        if not self.capacity == int:
            raise TypeError("Must be an integer or a cookies")
        if not self.capacity >= 0:
            raise ValueError("Cannot be a negative number")
        if self.capacity <= capacity:
            print()
        else:
            raise ValueError("Maxium amount reached")

    def __str__(self):

        self = int(input())
        cookies = self * "🍪"
        return cookies

    def deposit(self, n, cookies):
        jar = 0
        self.n = jar + cookies
        if len(self) > 12:
            raise ValueError("Maxium amount reached")

    def withdraw(self, n):
        withdraw = int(input())
        self = len(n) - withdraw
        if self <= 0:
            raise ValueError("No more cookies")

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self == 0
