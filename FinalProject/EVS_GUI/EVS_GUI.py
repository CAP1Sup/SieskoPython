# Christian Piper
# 11/21/19
# This program will generate a GUI in which the user can input the parameters. 
# The parameters will be used to create a code file that can be run on any Linux machine

# Constants
maxTitles = 3

# Variables
tagCount = 10

# Import GUI library and Picture Library
import tkinter as tk
from PIL import ImageTk,Image
import os


# Create GUI instance
gui = tk.Tk()

def main():
    # Setup parameters
    setupGUI()

    try:
        gui.mainloop()
    except SystemExit:
        print("Thank you for using Team 834's vision generator!")

# Function to generate the GUI
def setupGUI():

    # Setup window paramters
    gui.title("Easy Machine Learning Vision Generator")
    gui.geometry("900x800")

    # Description
    createLabel("This GUI will create the necessary files to run neural networks. Created by FRC Team 834.", 0, 0, False)  

    createImage('/Images/logo.jpg', 600, 0, 300, 200)

    # Tag title
    createLabel("Tags (from neural network)", 5, 25, True)

    # Tag Boxes
    spacing = 30
    list_start = 55
    tag = []
    for entry in range(0, tagCount - 1):
        tag.append(CreateEntry(5, (list_start + (spacing * entry)), True))


    spinBox_spacing = 30
    spinBox_list_start = 55
    spinBox = []
    for entry in range(0, tagCount - 1):
        spinBox.append(CreateSpinBox(3, 0, 10, 200, (spinBox_list_start + (spinBox_spacing * entry)), True))

    # Team number title
    createLabel("Team Number", 440, 25, True)

    # Team number box
    team_num = CreateEntry(400, 55, True)

    tagValues = []
    for entry in range(0, len(tag)):
        tagValues.append(tag[entry].get())

    # Create button for generating code files
    generateButton = tk.Button(gui, text = "Generate files", command = generateFiles(tagValues), font = 'Helvetica 20 bold')
    generateButton.place(x = 730, y = 765)

def generateFiles(tags):

    endingValue = 0

    for entry in range(0, len(tags)):
        if not tags[entry] == "":
            continue
        else:
            endingValue = entry
            break
    
    print(endingValue)

def addBox(currentVal):
    print("")

def createImage(path, x_location, y_location, x_size, y_size):
    size = (x_size, y_size)
    image =  Image.open( os.path.dirname(os.path.abspath(__file__)) + path)
    image.resize(size)
    tk_image = ImageTk.PhotoImage( image )
    img = tk.Label(gui, image = tk_image)
    img.image = tk_image
    img.place(x = x_location, y = y_location)

def createLabel(text, x_location, y_location, bold):
    if bold == True:
        label = tk.Label(gui, text = text, font = 'Helvetica 14 bold')
    else:
        label = tk.Label(gui, text = text)
    label.place(x = x_location, y = y_location)

def createMenuOption():
    pass

class CreateEntry:
    def __init__(self, x_location, y_location, visibility):
        self.entry = tk.Entry(gui)
        if visibility == True:
            self.entry.place(x = x_location, y = y_location)
        self.entry.x = x_location
        self.entry.y = y_location

    def get(self):
        return self.entry.get()

    def hide(self):
        self.entry.place_forget()

    def show(self):
        self.entry.place(x = self.entry.x, y = self.entry.y)

class CreateSpinBox:
    def __init__(self, width, from_, to, x_location, y_location, visibility):
        self.spinbox = tk.Spinbox(gui, from_ = from_, to = to, width = width)
        if visibility == True:
            self.spinbox.place(x = x_location, y = y_location)
        self.spinbox.x = x_location
        self.spinbox.y = y_location

    def get(self):
        return self.spinbox.get()

    def hide(self):
        self.spinbox.place_forget()

    def show(self):
        self.spinbox.place(x = self.spinbox.x, y = self.spinbox.y)
        
main()