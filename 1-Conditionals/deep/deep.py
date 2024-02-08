def main():
    x = input(
        "What is the real anwswer to the Great Question of Life, the Universe and Everything."
    )
    y = x.lower().replace("-", "").replace(" ", "")
    if y == "fortytwo" or y == "42":
        print("Yes")
    else:
        print("No")


main()
