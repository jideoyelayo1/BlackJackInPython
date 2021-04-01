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
userMoney = 5000
userMoneyBeingPutDown = 0

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
    while not(computerSum > 20 or userSum > 20):
        userInput = "2"
        if userInput == "C" or userInput == "c" or userMoney == 0:
            if userMoney == 0:
                print("You have no money")
                print("The House Has Beat You")
            sys.exit('Goodbye come again')
        while not (userInput == "Y" or userInput == "N" or userInput == "D"):
            print("Your total money is: "+ str(userMoney))
            if userMoneyBeingPutDown == 0:
                print("How much are you betting?")
                while userMoney < userMoneyBeingPutDown or userMoneyBeingPutDown == 0:
                    userMoneyBeingPutDown = int(input())

            print("Press Y to Hit or Press N to hold or Press D to Double-Hit")
            userInput = str(input())
            if userInput == "C" or userInput == "c":
                sys.exit('Goodbye come again')
            if userInput == "D":
                if userMoney > userMoneyBeingPutDown*2:
                    userMoneyBeingPutDown *= 2
                else:
                    print("You dont have that much money")
                    userInput = "2"


        if userInput == "Y" or userInput == "y":
            userPick = picksCard()
            userSum += userPick
            print("You picked a: " + str(userPick))
            print("Your total is " + str(userSum))
        if userInput == "N" or userInput == "n" or userStoppedPlaying:
            userStoppedPlaying = True
            if compStoppedPlaying:
                if 22 > userSum > computerSum:
                    userWon = True
                    compWon = False
                    break
                elif 22 > computerSum > userSum:
                    userWon = False
                    compWon = True
                    break
                elif userSum > 21:
                    compWon = True
                    break
                elif computerSum > 21:
                    userWon = False
                    break
            if 22 > computerSum > userSum:
                compWon = True
                break

            if userStoppedPlaying and compStoppedPlaying:
                print("Oh", end="")
                time.sleep(0.2)
                print("You both stopped playing")
                if 22 > userSum > computerSum:
                    userWon = True
                    compWon = False
                    break
                elif 22 > computerSum > userSum:
                    userWon = False
                    compWon = True
                    break
        if compAlgo() and not compStoppedPlaying:
            compPick = picksCard()
            computerSum += compPick
            print("Computer picked a: " + str(compPick))
            print("Computer total is " + str(computerSum))
        elif not compAlgo():
            compStoppedPlaying = True



        if (compStoppedPlaying and userStoppedPlaying) or computerSum > 20 or userSum > 20:
            if computerSum == 21 and userSum == 21:
                compWon = True
                userWon = True
                break
            elif computerSum > 21 and userSum < 21:
                compWon = False
                userWon = True
                break
            elif computerSum < 21 and userSum > 21:
                compWon = True
                userWon = False
                break
            elif computerSum == 21:
                compWon = True
                break
            elif userSum == 21:
                userWon = True
                break
            elif computerSum > userSum:
                compWon = True
                break
            elif computerSum < userSum:
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
        userMoney -= userMoneyBeingPutDown
    elif userWon:
        print("You won")
        userWins += 1
        userMoney += userMoneyBeingPutDown
    elif userMoney == 0:
        print("that was a bad bet")
        sys.exit('You lost all your money')
    print("Your Money is: " + str(userMoney))
    userMoneyBeingPutDown = 0

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
    if userMoney >= 100000:
        print("Woah You basically have beat the house")
    elif userMoney >= 5000:
        print("you doing well at beating the house")
    elif userMoney <= 500:
        print("You've made big losses quit for your own good")
    elif userMoney <= 250:
        print("You're going to run our of money soon")
    elif userMoney <= 100:
        print("The House has also beat, Maybe this Game isn't for you")
    print("Do you want to play again? Yes(Y) or No(N)")
    print("Press C to exit")
    userInput = "2"
    while not (userInput == "Y" or userInput == "y"):
        userInput = str(input())
        if userInput == "N":
            messageForWhenNo = "Oh that's okay press Y when you want to play or C if you want to leave the game"
            for i in range(0, len(messageForWhenNo)):
                print(messageForWhenNo[i], end = '')
                time.sleep(0.0759493670886076)
            print("")

        if userInput == "C" or userInput == "c":
            sys.exit('Goodbye come again')
#Made by TrimlessJay :]
