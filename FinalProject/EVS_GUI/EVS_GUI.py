# Christian Piper
# 11/21/19
# This program will generate a GUI in which the user can input the parameters. 
# The parameters will be used to create a code file that can be run on any Linux machine

# Constants
maxTitles = 3
tagCount = 10
top_row_offset = 55
first_entry_box_offset = 30

# Variables
fileDir = ""
tag = []
spinBox = []

# Import GUI library and Picture Library
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image
import csv
import os

# Create GUI instance
gui = tk.Tk()

# Assign current directory
currentDir = os.path.dirname(os.path.abspath(__file__))

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
    gui.title("Edge Vision System Code Generator")
    gui.geometry("900x800")
    
    # Create menu
    menu = tk.Menu(gui)
    fileMenu = tk.Menu(menu, tearoff=0)
    fileMenu.add_command(label="Select Directory", command = selectDir)
    fileMenu.add_separator()
    fileMenu.add_command(label="Save values", command = saveSettings)
    fileMenu.add_command(label="Load values", command = loadSettings)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command = gui.quit)
    menu.add_cascade(label="File", menu = fileMenu)

    gui.config(menu = menu)

    # 
    createLabel("EVS Code Generator", 150, 0, 900, 'c', 'Courier 48 bold')

    # Declare description variable so that the code isn't cluttered with long text
    description = getTextFile("/resources/text/description.txt")

    # Description
    createLabel(description, 350, 695, 525, 'l', 'Helvetica 14')  

    # Logo
    createImage('/resources/images/logoNoBack.png', 0, 695, .5)

    # Tag title
    createLabel("Tags (from neural network)", 5, top_row_offset, 200, 'l', 'Helvetica 14 bold')

    # Tag Boxes
    spacing = 30
    list_start = top_row_offset + first_entry_box_offset
    
    global tag
    for entry in range(0, tagCount - 1):
        tag.append(CreateEntry(5, (list_start + (spacing * entry)), True))

    # SpinBox label
    createLabel("Maximum Instances", 240, top_row_offset, 200, 'l', 'Helvetica 14 bold')

    # SpinBoxes for max instances
    spinBox_spacing = 30
    spinBox_list_start = top_row_offset + first_entry_box_offset
    
    global spinBox
    for entry in range(0, tagCount - 1):
        spinBox.append(CreateSpinBox(3, 0, 10, 275, (spinBox_list_start + (spinBox_spacing * entry)), True))

    # Team number title
    createLabel("Team Number", 440, top_row_offset, 200, 'l','Helvetica 14 bold')

    # Team number box
    team_num = CreateEntry(400, top_row_offset + first_entry_box_offset, True)

    tagValues = []
    for entry in range(0, len(tag)):
        tagValues.append(tag[entry].get())

    # Create button for generating code files
    #generateButton = tk.Button(gui, text = "Generate files", command = generateFiles(tagValues), font = 'Helvetica 20 bold')
    #generateButton.place(x = 730, y = 765)


def getTextFile(path):
    global currentDir
    file = open(currentDir + path, "r")
    text = file.read()
    return text


def selectDir():
    # Select directory and save the path of the save directory
    fileDir = filedialog.askdirectory(parent = gui, initialdir = "/",title = "Select save location")
    return fileDir


def selectFile():
    # Select a file
    fileDir = filedialog.askopenfilename(parent = gui, initialdir = "/", title = "Select save location", format = (".csv"))
    return fileDir


def saveSettings():
    # Select a directory
    dir = selectDir()

    # Store the settings in a .csv file
    with open(dir + 'EVS_settings.csv', mode='w') as settingsFile:

        fieldnames = ['tag', 'instance_number']
        writer = csv.DictWriter(settingsFile, fieldnames = fieldnames)

        global tag
        global spinBox

        writer.writeheader()
        for entry in range(0, tagCount - 1):
            writer.writerow({'tag': tag[entry].get(), 'instance_number': spinBox[entry].get})

def loadSettings():
    # Select a directory
    dir = selectDir()
    file = dir + 'EVS_settings.csv'

    global tag
    global spinBox

    # Load the settings from a .csv file
    with open(file, mode='r') as settingsFile:
        reader = csv.DictReader(settingsFile)
        lineCount = 0
        for row in reader:
            if lineCount == 0:
                lineCount += 1
            else:
                tag[lineCount].set({row["tag"]})
                spinBox[lineCount].set({row["instance_number"]})
                lineCount += 1


def onDirError(self):
    tk.messagebox.showerror("Error", "Could not open file")


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


def createImage(path, x_location, y_location, scale):
    global currentDir
    image =  Image.open( currentDir + path)
    width, height = image.size
    width = round(width * scale)
    height = round(height * scale)
    size = (width, height)
    resized = image.resize(size)
    tk_image = ImageTk.PhotoImage( resized )
    img = tk.Label(gui, image = tk_image)
    img.image = tk_image
    img.place(x = x_location, y = y_location)


def createLabel(text, x_location, y_location, max_width, justification, font):
    if justification == "l":
        justification = "left"
    elif justification == "r":
        justification = "right"
    elif justification == "c":
        justification = "center"

    label = tk.Label(gui, text = text, font = font, wraplength = max_width, justify = justification)
    label.place(x = x_location, y = y_location)


class CreateEntry:
    def __init__(self, x_location, y_location, visibility):
        self.entry = tk.Entry(gui)
        if visibility == True:
            self.entry.place(x = x_location, y = y_location)
        self.entry.x = x_location
        self.entry.y = y_location

    def get(self):
        return self.entry.get()
    
    def set(self, value):
        self.entry.insert(0, value)

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


if __name__ == '__main__':
    main()