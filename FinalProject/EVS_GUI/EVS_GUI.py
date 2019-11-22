# Christian Piper
# 11/21/19
# This program will generate a GUI in which the user can input the parameters. 
# The parameters will be used to create a code file that can be run on any Linux machine

# Constants
maxTitles = 3

# Variables
tagCount = 1

# Import GUI library and Picture Library
from tkinter import *
from PIL import ImageTk,Image
import os


# Create GUI instance
gui = Tk()

def main():
    # Setup parameters
    setupGUI()

    gui.mainloop()

# Function to generate the GUI
def setupGUI():

    # Setup window paramters
    gui.title("Easy Machine Learning Vision Generator")
    gui.geometry("1000x800")

    description = Label(gui, text = "This GUI will create the necessary files to run neural networks. Created by FRC Team 834.")  
    description.grid(column = 0, row = 0)

    createImage('/Images/logo.jpg', 800, 0, 300, 200)

    tagTitle = Label(gui, text = "Tags (from neural network)")
    tagTitle.grid(column = 0, row = 3)

    tag1 = Entry(gui, width = 20)
    tag1.grid( column = 0, row = 5)

def addBox(currentVal):
    print("")

def createImage(path, x_location, y_location, x_size, y_size):
    image = ImageTk.PhotoImage( Image.open( os.path.dirname(os.path.abspath(__file__)) + path) )
    # image.resize(x_size, y_size)
    img = Label(gui, image = image)
    img.image = image
    img.place(x = x_location, y = y_location)

main()