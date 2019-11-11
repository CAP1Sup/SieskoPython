# Christian Piper
# 11/1/19
# This program will accept 5 test grades (in percentage) and find the letter and average of all of the grades

def main():
    # Create names and results lists
    namings = ["first", "second", "third", "fourth", "fifth"]
    result = ["", "", "", "", ""]

    # Go through 5 times to get each test score
    for entry in range(0,5):
        result[entry] = input("Input your " + namings[entry] + " test grade: ")
        result[entry] = convertToInt(result[entry])
        print("Your grade was a " + str( getLetterGrade( result[entry] ) ))

    # Calculate the averages
    averageResult = calcAverage(result, 5, 2)

    print("The average grade was " + str(averageResult) + "%")
    print("The letter grade for the average was " + str( getLetterGrade(averageResult) ))

# Converts valid numbers to integers, otherwise it errors
def convertToInt(x):
    try:
        x = int(x)
    except:
        print("Issue converting! Make sure you are inputing valid numbers from 0-100!")
    return x

def calcAverage(results, num, decPlaces):

    total = 0

    for entry in range(0, num):
        total = total + results[entry]

    average = round(total / num, decPlaces)

    return average

def getLetterGrade(val):

    try: 
        val = int(val)
        
        # Count the number of each score
        if val < 60:
            grade = "F"
        elif val < 70:
            grade = "D"
        elif val < 80:
            grade = "C"
        elif val < 90:
            grade = "B"
        else:
            grade = "A"

        return grade

    except:
        print("Conversion error!")

main()