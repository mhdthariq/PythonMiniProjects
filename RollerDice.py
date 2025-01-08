import random

# Welcome message
print("Welcome to the Roller Dice Game!")

# Roller dice function
def roll():
    return random.randint(1, 6)

# Get number of players
def get_num_players():
    while True:
        players = input("Enter the number of players (2-4): ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                return players
            else:
                print("Number of players must be between 2 and 4.")
        else:
            print("Invalid input. Please enter a number.")

# Game setup
players = get_num_players()
max_score = players * 10
player_scores = [0] * players

# Main game loop
while max(player_scores) < max_score:
    for player_index in range(players):
        print(f"\nPlayer {player_index + 1}'s turn.")
        print(f"Current total score: {player_scores[player_index]}")
        current_score = 0

        # Player turn loop
        while True:
            should_roll = input("Roll the dice? (y/n): ").strip().lower()
            if should_roll == "y":
                value = roll()
                if value == 1:
                    print("Oops! You rolled a 1. Your turn is over!")
                    current_score = 0
                    break
                else:
                    current_score += value
                    print(f"You rolled a {value}. Current turn score: {current_score}.")
            elif should_roll == "n":
                print("Okay, skipping your turn.")
                break
            else:
                print("Invalid input. Please enter 'y' to roll or 'n' to end your turn.")

        player_scores[player_index] += current_score
        print(f"Total score after turn: {player_scores[player_index]}.")

# Determine winner
winning_score = max(player_scores)
winner = player_scores.index(winning_score) + 1
print(f"\nCongratulations! Player {winner} wins with a total score of {winning_score}!")