# Christian Piper
# 10/24/19
# This program will attempt to guess the password and report back the time taken to guess it
from time import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def main():
    pswd = input("Input your password: ")
    guessPassword(password = pswd, threads = 10, printTime = True, printpswd = True)

def guessPassword(password, threads, printTime, printpswd):
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
                        if printpswd:
                            print("The password was: " + str(total))
                        done = True
                        break


main()