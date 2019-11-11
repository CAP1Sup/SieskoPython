# Christian Piper
# 11/11/19
# This will accept algebra equations on the input and solve for the variable

def main():
    equation = input("Input your equation: ")
    variable = input("Input the variable to be solved for: ")

    solveAlgebraEquation(equation, variable)

def solveAlgebraEquation(equation, variable):

    collector = ["","","","","",""]
    iteration = 0

    for char in equation:
        
        if char == " " or char == "+" or char == "-" or char == "*" or char == "/" or char == ")" or char == "=" or char == "^":
            print(char + " - It's a separator!")
            iteration += 1
        else:
            collector[iteration] = collector[iteration] + char

    for count in range(0, iteration):
        print(collector[count])

main()