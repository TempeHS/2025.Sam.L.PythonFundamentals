def main():
    text_menu = ["1. Sang", "2. Chris", "3. Marcus", "4. Quit"]
    text_menu = "\n".join(text_menu)
    print(text_menu)
    while True:
        user_input = int(input("What do you want? "))
        if user_input == 1:
            print("Sang is a cool")
        elif user_input == 2:
            print("Chris is a bitch")
        elif user_input == 3:
            print("Marcus is gay")
        elif user_input == 4:
            print("Exitting")
            break
        else:
            print("Invalid input, please try again.")


if __name__ == "__main__":
    main()
