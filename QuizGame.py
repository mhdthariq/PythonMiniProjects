print("Welcome to the Computer Quiz Game!")

playing = input("Are you ready to play? (yes/no) ")

if playing.lower() != "yes":
    quit()

print("Let's play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does Motherboard stand for? ")
if answer.lower() == "main board":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + "/" + str(5) + " correct!")
print("Your final score is " + str((score / 5) * 100) + "%.")
