def main():
    fruit_calories = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapes": 90,
        "Honeydew Melon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet_Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80,
    }  # initialise a dictionary with fruit names and their calorie counts

    user_inputs = input(
        "Enter a fruit: "
    ).title()  # get user input and convert it to title case

    if user_inputs in fruit_calories:
        print(f"A {user_inputs} has {fruit_calories[user_inputs]} calories.")
    else:
        print(f"Sorry, we don't have the calorie count for {user_inputs}.")


main()
