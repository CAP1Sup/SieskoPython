# Christian Piper
# 11/6/19
# This is a file for all functions I create, so that they can be referenced from all files.
from time import time
import multiprocessing
import os

# Function for input to output conversion. For future use
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


# This is a password guessing function. You give it the current password, and it will find the password.
def guessPassword(password, printTime, printPswd, alphabet):
    '''
    :param password: The actual password
    :param printTime: T/F - Do you want to print the time taken?
    :param printPswd: T/F - Do you want to print the found password?
    :param alphabet: A string containing all the possible letters in the alphabet. Set to -1 to use built in dictonary.
    '''

    start = time()

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:',<.>/?"

    total = ""

    done = False

    #for i in len(password):
        # Run each value in
    for v1 in alphabet:
        if done:
            break
        for v2 in alphabet:
            if done:
                break
            for v3 in alphabet:
                if done:
                    break
                for v4 in alphabet:
                    total = v1 + v2 + v3 + v4
                    if total == password:
                        print("Successfully finished password!")
                        if printTime:
                            print("The time taken was: " + str(round(time() - start, 2)) + " seconds")
                        if printPswd:
                            print("The password was: " + str(total))
                        done = True
                        break

# This is a password guessing function. You give it the current password, and it will find the password.
def guessPasswordThreaded(password, threads, printTime, printPswd, alphabet):
    '''
    :param password: The actual password
    :param threads: The number of threads to use when guessing.
    :param printTime: T/F - Do you want to print the time taken?
    :param printPswd: T/F - Do you want to print the found password?
    :param alphabet: A string containing all the possible letters in the alphabet. Set to -1 to use built in dictonary.
    '''

    totalCharacters = ""
    
    if alphabet == -1:
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:',<.>/?"

    if os.path.exists("combinations.txt") == False:
        combinations = open("combinations.txt", "w")
        for firstChar in alphabet:
            for secondChar in alphabet:
                for thirdChar in alphabet:
                    for fourthChar in alphabet:
                        total = firstChar + secondChar + thirdChar + fourthChar
                        combinations.write(total + "\n")
        
        combinations.close()
    '''
    combinations = open("combinations.txt", "r")
    
    

    splitCombinations = [alphabet[i:i+threads] for i in range(0, len(alphabet), threads)]
    for count in range(1, threads):
        guessPassword(password, printTime, printPswd, splitAlphabet[count])
        f = multiprocessing.Process(target = guessPassword, args = (password, printTime, printPswd, splitAlphabet[count],)) 
        f.start

    combinations.close()
    '''

guessPasswordThreaded("Yeet", 1, True, True, -1)