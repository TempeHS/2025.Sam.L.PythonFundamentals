import random

game_played = 0
while game_played <= 2:
    game_played += 1
    options = ["paper", "rock", "scissor"]
    player = None

    computer_choice = random.choice(options)
    player = input("Enter your choice (Rock, Paper, Scissor): ").lower()

    print(f"Player Choice: {player}")
    print(f"Computer choice: {computer_choice}")
    if not player in options:
        game_played = 0
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
print("GOOD GAME, GG")
