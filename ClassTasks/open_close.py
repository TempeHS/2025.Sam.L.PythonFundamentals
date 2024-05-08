def main():
    with open("myText.txt", "r") as file:
        for number in file:
            num = int(number)
            new_num = num + 1

    with open("myText.txt", "w") as file:
        file.write(f"{new_num}")


if __name__ == "__main__":
    main()
