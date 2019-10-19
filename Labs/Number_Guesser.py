# Christian Piper
# Date 10/18/19
# Program: Guess my Die KWM 10 Pts. This game will prompt the user for a number
# between 1 and 6 or -1 to end, the program will simulate rolling a die and
# compare the die face with the user answer if they are equal the
# program will print you win and you get a point. If the numbers are
# not equal the program will print you lose, and add 1 to the numbe
# of losses. The program will then prompt the user again, until the
# user enters a -1. When a -1 is entered the program will display
# the number of wins and the number of losses.

# Import random integer function
from random import randint

min = 1
max = 6

# getNumber from user
def getNumber(min, max):
    userVal = input("Enter a number from " + str(min) + "-" + str(max) + ". Enter 'quit' or -1 if you would like to exit. Input: ")
    return userVal


def main():

    # Create win and loss variables
    wincount = 0
    losscount = 0

    while True:

        # Create value with the random result
        randVal = randint(min, max)

        # Get the user's value
        userVal = getNumber(min = 1, max = 6)

        # Exit if the user indicates they would like to
        if userVal == "-1" or userVal == "quit" or userVal == "Quit" or userVal == "q" or userVal == "Q":
            break

        else:
            # Convert to an integer
            try:
                userVal = int(userVal)
                flag = True

            except:
                # If that fails, then ask the user for another value
                print("Enter a valid number from 1 - 6!")
                flag = False

            # If that succeeds, compare values and add score
            if flag == True:
                # Value is ok, so continue
                if randVal == userVal:
                    wincount = wincount + 1
                    print("You got it!")
                else:
                    losscount = losscount + 1
                    print("Try again! The value was " + str(randVal))
    
    print("Your win count was " + str(wincount))
    print("Your loss count was " + str(losscount))
    total = wincount + losscount
    print("The total number of games was " + str(total))


main()