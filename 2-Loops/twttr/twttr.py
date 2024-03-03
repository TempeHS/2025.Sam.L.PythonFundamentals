def main():
    user_input = input("Input: ")
    shorten(user_input)


def shorten(word):
    shortened = ""
    for letter in word:
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            shortened += letter
    return shortened


if __name__ == "__main__":
    main()
