import random

prompt = True

while prompt:
    options = ["paper", "rock", "scissor"]
    player = None

    computer_choice = random.choice(options)
    player = input("Enter your choice (Rock, Paper, Scissor): ").lower()

    print(f"Player Choice: {player}")
    print(f"Computer choice: {computer_choice}")
    if player != options:
        print("Try again!")
    elif player == computer_choice:
        print("Tie")
    elif player == "rock" and computer_choice == "scissor":
        print("You win")
    elif player == "paper" and computer_choice == "rock":
        print("You Win")
    elif player == "scissor" and computer_choice == "paper":
        print("You win")
    else:
        print("Computer win")
    play_again = input("You want to player again? (y/n):").lower()
    if not play_again == "y":
        prompt = False
print("GOOD GAME, GG")
