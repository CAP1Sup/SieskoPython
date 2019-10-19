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
myStr = ""

# Open file for writing
myFile = open("/Users/200239/Desktop/scores.txt", "w")

# Make sure the file opened
if (myFile):
    print("success!")

    # Use a for loop to generate a string of numbers separted by a newline
    for i in range(0,100001):
        myStr = myStr + str(randint(50, 100)) + "\n"

    # Generate the contents of the file.
    # Generate test scores
    myFile.write(myStr)

# Close file 
myFile.close()
