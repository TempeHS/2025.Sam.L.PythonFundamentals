def main():
    # Get time from the user
    answer = input("The time is: ")
    # Call the convert functions
    time = convert(answer)
    # Breakfast between 7:00 - 8:00
    if 7 <= time and time <= 8:
        print("Breakfast")
    # Lunch between 12:00 - 13:00
    elif 12 <= time and time <= 13:
        print("Lunch")
    # Dinner between 18:00 - 19:00
    elif 18 <= time and time <= 19:
        print("Dinner")
    else:
        print("It is not time to eat")


def convert(time):
    # Get hour and minute
    hours, minutes = time.split(":")
    # Convert time into float variable
    new_minutes = float(minutes) / 60
    # Return the result to main function
    return float(hours) + new_minutes


if __name__ == "__main__":
    main()
