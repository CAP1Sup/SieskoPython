""" 
Christian Piper
Date: 10/7/19
This program will call the randint(a,b) 10,000 times and count the number of 1's, 2's, and 3's that randint(a,b)
"""
def main():
    import random # randint(a,b) is defined in random

    # Declare counters
    counter = 0 # Counter will count the number of times the loop executes
    oneCounter = 0 # Count number of 1's
    twoCounter = 0 # Count number of 2's
    threeCounter = 0 # Count number of 3's

    # First while loop for those that haven't done them
    while counter < 10000:
        y = random.randint(1, 3)
        if y == 1:
            oneCounter += 1
        elif y == 2:
            twoCounter += 1
        else:
            threeCounter += 1
        counter = counter + 1
    
    #Print results
    print("First counter: ", oneCounter)
    print("Second counter:", twoCounter)
    print("Third counter: ", threeCounter)

main()