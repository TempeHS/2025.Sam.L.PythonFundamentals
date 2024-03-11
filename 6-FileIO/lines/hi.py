# This is the testing space


def main():
    number_square = int(input("What number you want to square? "))
    squared = finding_squared(number_square)
    print(squared)


def finding_squared(n):
    return n * n


main()
