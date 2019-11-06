# Christian Piper
# 10/24/19
# This program will attempt to guess the password and report back the time taken to guess it
from functions import guessPassword


def main():
    pswd = input("Input your password: ")
    # Run a password guess with the input password, 10 threads (experimental), print the time 
    # taken, print the password, and use the builtin dictionary
    guessPassword(pswd, True, True, -1)

main()