import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
        else:
            print("Level must be above 0")
    except:
        pass

random_num = random.randint(1, n)

while True:
    try:
        user_guess = int(input("Guess: "))
        if user_guess < random_num:
            print("Too small")
        elif user_guess > random_num:
            print("Too large")
        else:
            print("Just right!")
            break
    except:
        pass
