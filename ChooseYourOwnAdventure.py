print("Welcome to the Adventure Game!")

# Ask the player if they want to play or not
play = input("Do you want to play? (yes/no): ").lower()

if play == "yes":
    name = input("What is your name? ")
    print(f"Hello, {name}! Let's start your adventure!")

    answer = input("You're on a dirt road, and it has come to an end. You can go left or right. Which way will you go? (left/right): ").lower()

    if answer == "left":
        answer = input("You come to a lake. There is a boat and path around the lake. You can take the boat or walk around. Which way will you do? (boat/walk): ").lower()

        if answer == "boat":
            print("You row across the lake but encounter a storm. The boat capsizes, and you drown. Game Over!")
        elif answer == "walk":
            answer = input("You walk for a while and find a house. Do you enter the house or keep walking? (enter/walk): ").lower()

            if answer == "enter":
                print("You enter the house and find a treasure chest. You open it and find a golden coin! You win!")
            elif answer == "walk":
                print("You keep walking and find a monster. It eats you. Game Over!")
            else:
                print("Not a valid option. Game Over!")
        else:
            print("Not a valid option. Game Over!")

    elif answer == "right":
        answer = input("You come to a bridge, but it looks weak. Do you cross the bridge or head back? (cross/back): ").lower()

        if answer == "cross":
            answer = input("You carefully cross the bridge and see a treasure chest. Do you open it or leave it? (open/leave): ").lower()

            if answer == "open":
                print("You open the chest. The chest is full gold and jewels. You win!")
            elif answer == "leave":
                print("You leave the treasure and walk away safely. but miss out on riches. You survive, but no treasure for you. Game Over!")
            else:
                print("Not a valid option. Game Over!")
        elif answer == "back":
            print("You turn back and run into a monster. It eats you. Game Over!")
        else:
            print("Not a valid option. Game Over!")

    else:
        print("Not a valid option. Game Over!")

    print("Thanks for playing!")
else:
    print("Okay, goodbye!")