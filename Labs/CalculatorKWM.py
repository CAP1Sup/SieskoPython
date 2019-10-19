# Christian Piper
# 9/19/19
# This program will illustrate how to use
# try/except
# and
# or


def main():
    while True:
        operation = input("Enter an integer from 1-4:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")
        # Error checking
        # Did the user enter a #?
        try:
            # Try to convert to a number if it is valid
            # number all good, if no the EXCEPT will execute
            operation = int(operation)
        except:
            print("You must enter a number, please run the program again")
            # Ask if they would like to run the program again
            goOn = input("Do you need more calculations done? (y/n): ")
            if goOn == 'Y' or goOn == 'y' or goOn == 'Yes' or goOn == 'yes':
                continue
            else:
                break
            
        
        if not(operation == 1 or operation == 2 or operation == 3 or operation == 4):
            print("Please select a valid operation")
        else:
            # Ask the user for two integers
            num1 = input("Enter number 1: ")
            num2 = input("Enter number 2: ")

            # Verify the user has entered a number
            try:
                num1 = float(num1)
                num2 = float(num2)
            except:
                print("You must enter an integer, please run the program again")

            # Do math when done
            if operation == 1:
                print("The sum is", (num1 + num2))
            elif operation == 2:
                print("The difference is", (num1 - num2))
            elif operation == 3:
                print("The product is", (num1 * num2))
            elif operation == 4:
                try:
                    print("The quotent is", (num1 / num2))
                except:
                    print("You can't divide by 0, the answer is undefined")

        # Ask if they would like to run the program again
        goOn = input("Do you need more calculations done? (y/n): ")
        if goOn == 'Y' or goOn == 'y' or goOn == 'Yes' or goOn == 'yes':
            print("Restarting program...")
            continue
        else:
            print("Thank you for using the Piper calculator by Piper Industries!")
            break

main()
