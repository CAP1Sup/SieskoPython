# Christian Piper
# 9/5/19
# This program creates a GUI calculator, similar to the arithmetic assignment, but with a full blown GUI. The calculator can do sum, difference, product, quotent, and modulus

# Import GUI library 
from tkinter import *
# Create instance of GUI
gui = Tk()

def main():
    # Create window
    gui.title("Equation Calculator")
    gui.geometry("500x300")
    
    # Create the title line
    mainPrompt = Label(gui, text = "Please Input Your Equation:")  
    mainPrompt.grid(column = 0, row = 0)

    # Create the entry boxes
    equationBox = Entry(gui, width = 20)
    equationBox.grid( column = 0, row = 3)

    

    # Create the answer line
    answer = Label(gui, text = "Answer will be here")
    answer.grid( column = 0, row = 9)

    # Create command for grabbing values from boxes

    '''
    # Make button commands
    def calculateSum():
        # Calculate sum
        sum = str(updateB1() + updateB2())
        # Set answer line to sum
        answer.configure(text = "Sum: " + sum)
    # Create button and assign location and command
    calculateSumButton = Button(gui, text = "Calculate Sum", command = calculateSum)
    calculateSumButton.grid(column = 10, row = 0)

    def calculateDifference():
        # Calculate difference
        difference = str(updateB1() - updateB2())
        # Set answer line to difference
        answer.configure(text = "Difference: " + difference)
    # Create button and assign location and command
    calculateDifferenceButton = Button(gui, text = "Calculate Difference", command = calculateDifference)
    calculateDifferenceButton.grid(column = 10, row = 3)

    def calculateAbsoluteDifference():
        # Calculate difference
        absoluteDifference = str( abs (updateB1() - updateB2()) )
        # Set answer line to difference
        answer.configure(text = "Absolute Difference: " + absoluteDifference)
    # Create button and assign location and command
    calculateAbsoluteDifferenceButton = Button(gui, text = "Calculate Absolute Difference", command = calculateAbsoluteDifference)
    calculateAbsoluteDifferenceButton.grid(column = 10, row = 6)

    def calculateProduct():
        # Calculate product
        product = str(updateB1() * updateB2())
        # Set answer line to product
        answer.configure(text = "Product: " + product)
    # Create button and assign location and command
    calculateProductButton = Button(gui, text = "Calculate Product", command = calculateProduct)
    calculateProductButton.grid(column = 10, row = 9)

    def calculateQuotent():
        # Calculate quotent
        quotent = str(updateB1() / updateB2())
        # Set answer line to quotent
        answer.configure(text = "Quotent: " + quotent)
    # Create button and assign location and command
    calculateQuotentButton = Button(gui, text = "Calculate Quotent", command = calculateQuotent)
    calculateQuotentButton.grid(column = 10, row = 12)

    def calculateMod():
        # Calculate modulus
        mod = str(updateB1() % updateB2())
        # Set answer line to modulus
        answer.configure(text = "Modulus: " + mod)
    # Create button and assign location and command
    calculateModButton = Button(gui, text = "Calculate Mod", command = calculateMod)
    calculateModButton.grid(column = 10, row = 15)
    '''
    
    gui.mainloop()

main()