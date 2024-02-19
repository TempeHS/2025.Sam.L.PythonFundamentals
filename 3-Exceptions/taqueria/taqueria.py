# Create a function that add up the ordering
def check_in():
    # Start with zero because that how it works
    total_amount = 0
    # Loop while making sure the user input will be ask again
    while True:
        item = input("Item: ").strip().title()
        if item in menu:
            # Adding the input from the menu price
            total_amount += menu[item]
            print(f"Total: ${total_amount:.2f}")
        # Break out of loop if user input q
        elif item.lower() == "q":
            print("Exiting...")
            break
        # If not on the list the, it will print the bottom line
        else:
            print("Invalid item. Please try again.")


if __name__ == "__main__":
    menu = {
        # Menu list
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
