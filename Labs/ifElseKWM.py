""" This is the start of a multiline comment

Christian Piper
9/17/19
This program will prompt the user for 3 text scores
and calculate the average and letter grade.

The end of a multiline comment """ 

def main():
    #Get the information the user
    t1 = input("Enter test 1: ")
    t2 = input("Enter test 2: ")
    t3 = input("Enter test 3: ")

    #Convert to a number type
    t1 = float(t1)
    t2 = float(t2)
    t3 = float(t3)

    #Calculate average
    average = (t1 + t2 + t3) / 3
    #Store the letter grade in letter (default case)
    letter = ' " '
    #Find the letter grade
    if average < 60:
        letter = 'F'
    elif average < 70:
        letter = 'D'
    elif average < 80:
        letter = 'C'
    elif average < 90:
        letter = 'B'
    elif average >= 90:
        letter = 'A'

    #Print the results
    print("The average is: ", average)
    print("The letter grade is: ", letter)

main()