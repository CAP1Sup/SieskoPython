# Christian Piper
# 9/5/19
# This program will prompt the user for miles driven and gallons used 4 times. It will then output the total miles driven,
# total gallons used, and the average miles per gallon of the trip

def main():
    # Create prompts for inputs and convert to floating point numbers
    miles1 = float(input("Enter miles travelled: "))
    gallons1 = float(input("Enter gallons of gas used: "))
    print() # Print() statements are used to add lines in between the prompts
    miles2 = float(input("Enter miles travelled: "))
    gallons2 = float(input("Enter gallons of gas used: "))
    print()
    miles3 = float(input("Enter miles travelled: "))
    gallons3 = float(input("Enter gallons of gas used: "))
    print()
    miles4 = float(input("Enter miles travelled: "))
    gallons4 = float(input("Enter gallons of gas used: "))
    print()

    # Do calculations
    totalMiles = miles1 + miles2 + miles3 + miles4
    totalGallons = gallons1 + gallons2 + gallons3 + gallons4
    averageMPG = totalMiles / totalGallons

    # Convert floating points to strings
    totalMiles = str(totalMiles)
    totalGallons = str(totalGallons)
    averageMPG = str(averageMPG)

    # Print results
    print("You drove " + totalMiles + " miles")
    print("You used " + totalGallons + " gallons")
    print("Your average MPG was " + averageMPG)

main()