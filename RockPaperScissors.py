import random

print("Welcome to the Rock Paper Scissors Game!")

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter 'rock', 'paper', 'scissors', or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_choice = options[random_number]
    print(f"Computer chose {computer_choice}.")

    if user_input == "rock" and computer_choice == "scissors":
        print("You win!")
        user_wins += 1
    elif user_input == "paper" and computer_choice == "rock":
        print("You win!")
        user_wins += 1
    elif user_input == "scissors" and computer_choice == "paper":
        print("You win!")
        user_wins += 1
    elif user_input == computer_choice:
        print("It's a tie!")
    else:
        print("You lose!")
        computer_wins += 1

print("Thanks for playing! Your final score is:")
print(f"You: {user_wins}")
print(f"Computer: {computer_wins}")
print("Goodbye!")

