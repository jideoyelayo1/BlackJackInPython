import random
import time
import sys

# variables
computerSum = 0
userSum = 0
cards = []
userStoppedPlaying  = False
compStoppedPlaying =  False
userWon = False
compWon = False
compWins = 0
userWins = 0

#Build Cards
for i in range(1,14):
    for j in range(0,4):
        cards.append(i)
#functions
def refillCards():
    global cards
    for i in range(1, 14):
        for j in range(0, 4):
            cards.append(i)
def compAlgo():
    global computerSum
    global userSum
    global userStoppedPlaying
    cardsNeededToWin = 21 - computerSum
    if computerSum > userSum and not userStoppedPlaying:
        return False
    if cardsNeededToWin > random.randint(1,13):
        return True
    else:
        return False
def picksCard():
    global cards
    if len(cards) < 30:
        refillCards()
    index = random.randint(0, len(cards) - 1)
    cardPicked = cards[index]
    cards.pop(cardPicked)
    return cardPicked


# Main()
print("Press X to start ")
print("Press C to cancel at anytime")
userInput = "2"
while not userInput == "X" or userInput == "x":
    userInput = str(input())
    if userInput == "C" or userInput == "c":
        sys.exit('Goodbye come again')
print("Yay")
time.sleep(0.5)
print("Let's begin")
while True:
    while (not (userSum > 20)) and (not (computerSum > 20)):

        while not userInput == "Y" or userInput == "y" or userInput == "N" or userInput == "n":
            print("Press Y to draw and Press N to stop")
            userInput = str(input())
            if userInput == "C" or userInput == "c":
                sys.exit('Goodbye come again')
        if userInput == "Y" or userInput == "y":
            userPick = picksCard()
            userSum += userPick
            print("You picked a: " + str(userPick))
            print("Your total is " + str(userSum))
        elif userInput == "N" or userInput == "n":
            userStoppedPlaying = True
        if compAlgo():
            compPick = picksCard()
            computerSum += compPick
            print("Computer picked a: " + str(compPick))
            print("Computer total is " + str(computerSum))
        elif not compAlgo():
            compStoppedPlaying = True

        if compStoppedPlaying or userStoppedPlaying or computerSum > 20 or userSum > 20:
            if computerSum == 21 and userSum == 21:
                compWon = True
                userWon = True
                break
            elif computerSum == 21:
                compWon = True
                break
            elif userSum == 21:
                userWon = True
                break
            elif compStoppedPlaying and computerSum > userSum:
                compWon = True
                break
            elif compStoppedPlaying and computerSum < userSum:
                userWon = True
                break
        userInput = "1"

    for i in range(10):
        print('.', end='')
        time.sleep(0.2)
    print("")

    print("computer total is " + str(computerSum))
    print("user total is " + str(userSum))

    if compWon and userWon:
        print("you tied")
    elif compWon:
        print("Computer Wins")
        compWins += 1
    elif userWon:
        print("You won")
        userWins += 1

    computerSum = 0
    userSum = 0
    userStoppedPlaying = False
    compStoppedPlaying = False
    userWon = False
    compWon = False

    for i in range(10):
        print('-', end='')
        time.sleep(0.1)
    print("")
    print("You " + str(userWins) + " Com "+str(compWins))
    print("")

#Made by TrimlessJay :]
