import sys


def main(input_str):
    print("Output: " + shorten(input_str))


def shorten(word):
    shortened = ""
    for letter in word:
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
            shortened += letter
    return shortened


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Error: please provide an input string as a command-line argument")
