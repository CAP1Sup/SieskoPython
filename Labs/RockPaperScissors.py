# Christian Piper
# 11/4/19
# This program allows the user to play rock, paper, scissors against a computer

# Import random integer function
from random import randint

def convertValues(inputVal, inputArray, outputArray, wrapAround):
    '''
    :param inputVal: The value being converted
    :param inputArray: An array of values to convert from
    :param outputArray: An array of values to output in alignment with the input array
    :param wrapAround: Set to True to wrap around the output array if the value is out of range. Otherwise it will raise an error
    '''

    # Check all entries in the input array and compare them to the input value
    for entry in range(0, len(inputArray)):
        # If the value is a match, return the equivient from the output array
        if inputArray[entry] == inputVal:
            # Wrap around the output if the value is out of range
            if wrapAround:
                wrapAroundEntry = entry % len(outputArray)
                return outputArray[wrapAroundEntry]
            else:
                try:
                    return outputArray[entry]
                except:
                    print(
                        "The input array listing is out of the range of the output array's")
    
    print("The input value was not found. Make sure that you are using the correct value.")

def main():
    while True:
        # Set up the computer's guess
        rawComputerPlay = randint(1, 3)
    
        # Set up the arrays for the conversion factors
        computerInteger = [1, 2, 3]
        rockPaperScissorsCharacters = ['r', 'p', 's']
    
        # Convert the values from integers to characters
        computerPlay = convertValues(
            rawComputerPlay, computerInteger, rockPaperScissorsCharacters, False)

        # Get the user to input their play
        rawUserPlay = input(
            "Input your play. Please use 'rock', 'scissors', or 'paper'. You could also choose to end playing with 'stop' or 'end': ")
    
        # Check to see if the user wants to exit, and exit the loop if they do
        if rawUserPlay == 'stop' or rawUserPlay == 'end':
            break

        plays = ['rock.', 'paper.', 'scissors.']

        print("The computer's play was " + convertValues(computerPlay, rockPaperScissorsCharacters, plays, False))
        # Set up arrays for the conversion from words to numbers
        words = ["rock", "paper", "scissors", "r", "p", "s"]
    
        # Convert the words into characters for easier comparison
        userPlay = convertValues(rawUserPlay, words, rockPaperScissorsCharacters, True)
    
        # Get result from matchup
        result = findRockPaperScissorsResult(userPlay, computerPlay)
    
        # Convert the result to nice printouts
        possibleResults = ['w', 't', 'l']
        printOutputs = ["You won!", "You tied with the computer!", "You lost!"]

        # Print what the end result was
        print(convertValues(result, possibleResults, printOutputs, False))
        print()


def findRockPaperScissorsResult(a, b):
    '''
    Wins, ties, and losses are from a's perspective
    :param a: The input of the first user in integers
    :param b: The input of the second user in integers
    '''

    # Means that they are both the same, resulting in a tie
    if a == b:
        return 't'

    # Rock crushes scissors, resulting in a win for a
    elif a == 'r' and b == 's':
        return 'w'

    # Scissors cuts paper, resulting in a win for a
    elif a == 's' and b == 'p':
        return 'w'

    # Paper covers rock, resulting in a win for a
    elif a == 'p' and b == 'r':
        return 'w'

    # Rock crushes scissors, resulting in a win for b
    elif a == 's' and b == 'r':
        return 'l'

    # Scissors cuts paper, resulting in a win for b
    elif a == 'p' and b == 's':
        return 'l'

    # Paper covers rock, resulting in a win for b
    elif a == 'r' and b == 'p':
        return 'l'


main()
