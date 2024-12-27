import random

print("Welcome to the Number Guessing Game!")

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number greater than 0.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guess_count = 0

while True:
    guess_count += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You guessed the number!")
        break
    elif user_guess > random_number:
        print("Too high.")
    else:
        print("Too low.")

print("You guessed the number in", guess_count, "guesses.")