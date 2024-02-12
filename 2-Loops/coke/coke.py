def main():
    while True:
        amounts = int(input("Insert coin (25, 5, or 10 cents only): "))
        if amounts == 25 or amounts == 5 or amounts == 10:
            break
        print("Invalid input. Amount Due: 50")

    remain = coin_counter(amounts)
    print(remain)

    while remain > 0:
        print(f"Amount Due: {remain}")
        cent = int(input("Amount Due:"))
        if cent == 10 or cent == 25 or cent == 5:
            remain -= cent
        else:
            print("Invalid coin. Please insert a valid coin (10, 25, or 5 cents).")

    print(f"Change owed: {abs(remain)}")


def coin_counter(amounts):
    remain = 50 - amounts
    return remain


if __name__ == "__main__":
    main()
