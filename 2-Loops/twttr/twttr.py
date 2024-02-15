def main():
    user_texts = input("Input: ")
    print("Output:", end="")
    for letter in user_texts:
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            print(letter, end="")

    print()


main()
