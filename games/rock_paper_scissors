# Darius Corbin
# 1/21/2023
# Rock, Paper, Scissors Game

import random

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"

    if player_choice == "rock":
        if computer_choice == "paper":
            return "computer"
        else:
            return "player"

    if player_choice == "paper":
        if computer_choice == "scissors":
            return "computer"
        else:
            return "player"

    if player_choice == "scissors":
        if computer_choice == "rock":
            return "computer"
        else:
            return "player"

print("Let's play Rock, Paper, Scissors!")

# Ask the user if they want to play best 2 out of 3.
best_of_3 = input("Do you want to play best 2 out of 3? (y/n)").lower() == "y"
player_score = 0
computer_score = 0

while True:
    print("Make your choice: (r)ock, (p)aper, (s)cissors or (q)uit")
    player_choice = input("> ").lower()

    if player_choice == "q":
        print("Thanks for playing!")
        break

    if player_choice not in ["r", "p", "s"]:
        print("Invalid choice, try again.")
        continue

    # Map player choice to full name
    player_choice_name = {"r": "rock", "p": "paper", "s": "scissors"}[player_choice]

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chooses {computer_choice}")

    winner = get_winner(player_choice_name, computer_choice)

    if winner == "player":
        print("You win!")
        player_score += 1
    elif winner == "computer":
        print("Computer wins!")
        computer_score += 1
    else:
        print("It's a tie!")

    # Check if a player has won at least 2 games.
    if player_score == 2 or computer_score == 2:
        if player_score > computer_score:
            print("Congratulations! You won the game.")
        else:
            print("Sorry, the computer won the game.")

        # Reset scores for new game.
        player_score = 0
        computer_score = 0

        # Ask the user if they want to play again.
        play_again = input("Do you want to play again? (y/n)").lower() == "y"
        if not play_again:
            break

    elif best_of_3 and max(player_score, computer_score) < 2:
        continue
    else:
        if player_score > computer_score:
            print("Congratulations! You won the game.")
        elif computer_score > player_score:
            print("Sorry, the computer won the game.")
        else:
            print("The game ended in a tie.")

        # Reset scores for new game in best 2 out of 3 mode.
        if best_of_3:
            player_score = 0
            computer_score = 0
            continue
        else:
            break
