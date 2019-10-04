#Rock Paper Scissors
#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock

userOneName = input("Enter your name: \n")
userTwoName = input("Enter your name: \n")

userOne = input("%s, enter Rock, Paper or Scissors: \n" % userOneName)

userTwo = input("%s, enter Rock, Paper or Scissors: \n" % userTwoName)

if userOne == userTwo:
    print("It's a tie")
elif userOne == "rock":
    if userTwo == "scissors":
        print(userOneName, "beats", userTwoName)
    else:
        print(userTwoName, "beats", userOneName)
elif userOne == "scissors":
    if userTwo == "paper":
        print(userOneName, "beats", userTwoName)
    else:
        print(userTwoName, "beats", userOneName)
elif userOne == "paper":
    if userTwo == "rock":
        print(userOneName, "beats", userTwoName)
    else:
        print(userTwoName, "beats", userOneName)
else:
    print("Invalid input! You must enter Rock, Paper or Scissors")
    sys.exit()