def main():
    x = input("Greating: ").format().lower().strip()
    if x.startswith("hello"):
        print("$0")

    elif x.startswith("h"):
        print("$20")

    else:
        print("$100")


main()
