def check_in():
    total_amount = 0
    while True:
        item = input("Item: ").strip().title()
        if item in menu:
            total_amount += menu[item]
            print(f"Total: ${total_amount:.2f}")
        elif item.lower() == "q":
            print("Exiting...")
            break
        else:
            print("Invalid item. Please try again.")


if __name__ == "__main__":
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }
    check_in()
