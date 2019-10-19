# Christian Piper
# 9/5/19
# This program creates a gui calculator


from tkinter import *
gui = Tk()

def main():
    gui.title("Python Calculator")
    gui.geometry("1920x1080")
    mainTitle = Label(gui, text = "Please Input Some Numbers for Calculation")  
    mainTitle.grid(column = 0, row = 0)

    number1Box = Entry(gui, width = 20)
    number1Box.grid( column = 0, row = 3)

    number2Box = Entry(gui, width = 20)
    number2Box.grid( column = 0, row = 6)

    answer = Label(gui, text = "Answer will be here")
    answer.grid( column = 0, row = 9)

    def calculateSum():
        B1 = int(number1Box.get())
        B2 = int(number2Box.get())
        sum = B1 + B2
        answer.configure(text = sum)
    calculateSumButton = Button(gui, text = "Calculate Sum", command = calculateSum)
    calculateSumButton.grid(column = 10, row = 0)

    def calculateDifference():
        B1 = int(number1Box.get())
        B2 = int(number2Box.get())
        difference = B1 - B2
        answer.configure(text = difference)
    calculateDifferenceButton = Button(gui, text = "Calculate Difference", command = calculateDifference)
    calculateDifferenceButton.grid(column = 10, row = 3)

    def calculateProduct():
        B1 = int(number1Box.get())
        B2 = int(number2Box.get())
        product = B1 * B2
        answer.configure(text = product)
    calculateProductButton = Button(gui, text = "Calculate Product", command = calculateProduct)
    calculateProductButton.grid(column = 10, row = 6)

    def calculateQuotent():
        B1 = int(number1Box.get())
        B2 = int(number2Box.get())
        quotent = B1 / B2
        answer.configure(text = quotent)
    calculateQuotentButton = Button(gui, text = "Calculate Quotent", command = calculateQuotent)
    calculateQuotentButton.grid(column = 10, row = 9)

    def calculateMod():
        B1 = int(number1Box.get())
        B2 = int(number2Box.get())
        mod = B1 % B2
        answer.configure(text = mod)
    calculateModButton = Button(gui, text = "Calculate Mod", command = calculateMod)
    calculateModButton.grid(column = 10, row = 12)
    
    gui.mainloop()

main()
    


