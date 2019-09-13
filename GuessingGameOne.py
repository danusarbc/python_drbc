#Guessing Game One

#Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

randomNum = random.randint(1,9)

print("Try to guess the number!!!")
count = 0
numUser = 0

while numUser != randomNum and numUser != "exit":
    numUser = input("Enter a number 1 to 9!!! \n")
    if numUser == "exit":
        break
    numUser = int(numUser)
    count += 1
    if numUser < randomNum:
        print("Too low")
    elif numUser > randomNum:
        print("Too right")
    else:
        print("Congratulations!!! Exactly right. You got it in ", count, "tries")