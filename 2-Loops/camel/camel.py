def main():
    camel_case = input("camelCase: ").strip()
    print("snake_case: ", end="")
    for letter in camel_case:
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else:
            print(letter, end="")
    print()


if __name__ == "__main__":
    main()
