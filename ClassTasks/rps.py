import random

playerchoice = input("Enter your decision: ").lower


def computer_choice(x):
    computer_choice = ["paper" or "p", "rock" or "r", "scissor" or "s"]
    x = computer_choice
    print(random.choice(x))
    return x
