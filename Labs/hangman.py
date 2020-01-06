import random

def get_guess(secret_word):

    # Set the dashes to the length of the secret word and set the amount of guesses

    # The user has to 10
    dashes  = "-" * len(secret_word)
    guesses_left = 3
    print_person = 0

    print_hangman_name()
    print_figure()

    # This will loop as long as BOTH conditions are true:
    while guesses_left > -1 and not(dashes == secret_word):
        
        

        # Print the amount of dashes and guesses left
        print(dashes)
        print("Number of guesses left:", guesses_left)

        # Ask the user for input
        guess = input("Enter your guess: ")

        # Conditions that will print out a message according to invalid inputs
        if not(len(guess) == 1):
            print("Your guess must have exactly one character.")

        # If the guess is in the secret word then we update dashes to replace the corresponding dash with the correct index the guess belongs to in the secret word
        elif guess.lower() in secret_word.lower():
            # print("That letter is in the secret word.")
            dashes = update_dashes(secret_word, dashes, guess)

        # If the guess is wrong then we display a message and subtract the amount of guesses the user has by 1
        else:
            print("That letter is not in the secret word.")
            guesses_left = guesses_left - 1
        
        if guesses_left < 0:
            print("You lose. The word was: " + str(secret_word))

        # If the dash string equals the secret word in the end then the user wins
        elif dashes == secret_word:
            print("Congrats! You win. The word was: " + str(secret_word))

        else:
            print("Keep going!")
        
def update_dashes(secret_word, cur_dashes, guess):
    result = ""

    for i in range(len(secret_word)):
        if secret_word[i].lower() == guess.lower():
            result = result + secret_word[i] # Adds guess to string if guess is correct
        
        else:
            # Add the dash at index i to result if it doesn't match the guess
            result = result + cur_dashes[i]
        
    return result

def print_hangman_name():
    print()
    print("                    ____")
    print("|   |   /\   |\  | |    | |\    /|   /\   |\  | ")
    print("|---|  /--\  | \ | |  ___ | \  / |  /--\  | \ | ")
    print("|   | /    \ |  \| |____| |  \/  | /    \ |  \| ")
    print("Coded by: Christian Piper")


def print_figure():
    print()
    print("____________        ")
    print("|        __|__      ")
    print("|       / - - \     ")
    print("|      |   \   |    ")
    print("|       \ === /     ")
    print("|          |        ")
    print("|     -----|-----   ")
    print("|          |        ")
    print("|          |        ")
    print("|         / \       ")
    print("|        /   \      ")
    print("|       /     \     ")
    print()

def main():
    words = ["Snow", "Ice", "Fire", "Wind"]
    secret_word = random.choice(words)
    get_guess(secret_word)

main()