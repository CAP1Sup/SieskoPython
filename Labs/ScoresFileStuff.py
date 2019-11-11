# Christian Piper
# 10/16/19
# This program will generate 100,000 random numbers between 50 <= score <= 100
# Each of these scores will be written to a text file called scores.txt

""" 
In order to use files you always need to:
1) Open the file
2) Process the contents
3) Close the file

Two ways to open file:
1) r = reading =>   Can be read but not changed
2) w = writing =>   If the file exists in the contents are deleted
                    If the file doesn't exist, it will create it
"""
from random import randint

# Variables
scoreFilePath = "scores.txt"

def writeScores():

    scores = ""
    # Open file for writing
    scoreFile = open(scoreFilePath, "w")

    # Make sure the file opened
    if (scoreFile):
        print("success!")

        # Use a for loop to generate a string of numbers separted by a newline
        for i in range(0,100001):
            scores = scores + str(randint(50, 100)) + "\n"

        # Generate the contents of the file.
        # Generate test scores
        scoreFile.write(scores)
        print("The values have been written!")

    # Close file 
    scoreFile.close()



def readScores():

    # Create variables for counts
    fcount = 0
    dcount = 0
    ccount = 0
    bcount = 0
    acount = 0

    # Open score file for reading
    scoreFile = open(scoreFilePath, "r")

    # Make sure the file opened
    if (scoreFile):
        for line in scoreFile:

            # Try to convert to an integer
            try: 
                val = int(line)
        
                # Count the number of each score
                if val < 60:
                    fcount = fcount + 1
                elif val < 70:
                    dcount = dcount + 1
                elif val < 80:
                    ccount = ccount + 1
                elif val < 90:
                    bcount = bcount + 1
                else:
                    acount = acount + 1

            except:
                print("Make sure all the values are integers!")

        print("The number of As was", acount)
        print("The number of Bs was", bcount)
        print("The number of Cs was", ccount)
        print("The number of Ds was", dcount)
        print("The number of Fs was", fcount)
    
    scoreFile.close()

    print("Finished!")

writeScores()
#readScores()
