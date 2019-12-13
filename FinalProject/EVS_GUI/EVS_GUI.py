# Christian Piper
# 11/21/19
# This program will generate a GUI in which the user can input the parameters. 
# The parameters will be used to create a code file that can be run on any Linux machine

# TODO:
# Better comments
# help tab and files

# Import GUI library and Picture Library
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image # TODO: Write install script
import csv
import os
import generate_py_file

# Create GUI instance
gui = tk.Tk()

# Constants
maxTitles = 3
tagCount = 10
top_row_offset = 130
first_entry_box_offset = 30

# Variables
fileDir = ""
tag = []
spinBox = []
tag_list = [] 
instance_list = []
raw_team_number = None
neural_compute_stick = tk.BooleanVar()
print_info = tk.BooleanVar()
streamer = tk.BooleanVar()
dashboard_confidence = tk.BooleanVar()
neural_compute_stick_checkbox = None
print_info_checkbox = None
streamer_checkbox = None
dashboard_confidence_checkbox = None

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
    file_menu = tk.Menu(menu, tearoff = 0)
    file_menu.add_command(label="Save settings to file", command = saveSettings)
    file_menu.add_command(label="Load settings from file", command = loadSettings)
    file_menu.add_separator()
    file_menu.add_command(label="Save settings for next launch", command = saveLoadingSettings)
    file_menu.add_command(label="Reset launch settings", command = deleteLoadingSettings)
    file_menu.add_separator()
    file_menu.add_command(label="Generate code files", command = generateFiles)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command = gui.quit)
    menu.add_cascade(label="File", menu = file_menu)

    gui.config(menu = menu)

    # Declare description variable so that the code isn't cluttered with long text
    description = getTextFile("/resources/text/description.txt")

    # Description
    createLabel(description, 350, 0, 525, 'l', 'Helvetica 14')  

    # Logo
    createImage('/resources/images/logoNoBack.png', 0, 0, .5)

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
    global raw_team_number
    raw_team_number = CreateEntry(400, top_row_offset + first_entry_box_offset, True)

    global neural_compute_stick
    global neural_compute_stick_checkbox
    neural_compute_stick_checkbox = tk.Checkbutton(gui, text="Using Neural Compute Stick?", var = neural_compute_stick)
    neural_compute_stick_checkbox.config(wraplength = 300)
    neural_compute_stick_checkbox.place(x = 390, y = 200)

    global print_info
    global print_info_checkbox
    print_info_checkbox = tk.Checkbutton(gui, text="Print running info? This most likely will not save any processing power by disabling", var = print_info)
    print_info_checkbox.config(wraplength = 300)
    print_info_checkbox.place(x = 390, y = 263)

    global streamer
    global streamer_checkbox
    streamer_checkbox = tk.Checkbutton(gui, text="Use the streamer? This will cause a drop in framerate, but will be benefical for testing", var = streamer)
    streamer_checkbox.config(wraplength = 300)
    streamer_checkbox.place(x = 390, y = 326)

    global dashboard_confidence
    global dashboard_confidence_checkbox
    dashboard_confidence_checkbox = tk.Checkbutton(gui, text="View and modify confidence threshold on the SmartDashboard? (Beta! Use at your own risk!)", var = dashboard_confidence)
    dashboard_confidence_checkbox.config(wraplength = 300)
    dashboard_confidence_checkbox.place(x = 390, y = 390)

    # Create button for generating code files
    #generateButton = tk.Button(gui, text = "Generate files", command = generateFiles(tagValues), font = 'Helvetica 20 bold')
    #generateButton.place(x = 730, y = 765)

    save_file_path = "../EVS_GUI/resources/loading_parameters/EVS_settings.csv"
    if os.path.exists(save_file_path):
        loadSettings(save_file_path)

def getParameterValues():
    # Gets the values for all of the parameters

    # Load all of the universal values
    global raw_team_number
    global neural_compute_stick
    global print_info
    global streamer
    global dashboard_confidence

    # Get thier values and save them in _val variables
    raw_team_number_val = raw_team_number.get()
    neural_compute_stick_val = neural_compute_stick.get()
    print_info_val = print_info.get()
    streamer_val = streamer.get()
    dashboard_confidence_val = dashboard_confidence.get()

    # Return them as a string
    return raw_team_number_val, neural_compute_stick_val, print_info_val, streamer_val, dashboard_confidence_val


def getTextFile(path):
    global currentDir
    file = open(currentDir + path, "r")
    text = file.read()
    return text


def selectDir(title = "Select directory"):
    # Select directory and save the path of the save directory
    fileDir = filedialog.askdirectory(parent = gui, initialdir = "/",title = title)
    return fileDir


def selectFile(title = "Select file", file_ext = None):
    # Select a file
    if not file_ext == None:
        fileDir = filedialog.askopenfilename(parent = gui, initialdir = "/", title = title, defaultextension = file_ext)
    else:
        fileDir = filedialog.askopenfilename(parent = gui, initialdir = "/", title = title)
    return fileDir


def saveSettings(dir = None):
    # Select a directory
    if dir == None:
        dir = selectDir(title = "Select save location for settings:")

    # Store the settings in a .csv file
    with open(dir + '//EVS_settings.csv', mode='w+') as settingsFile:
        parameter_field_names = ['team_num', 'neural_compute_stick', 'print_info', 'streamer', 'dashboard_confidence']
        parameter_writer = csv.DictWriter(settingsFile, fieldnames = parameter_field_names)

        tag_and_instance_field_names = ['tag', 'instance_number']
        tag_and_instance_writer = csv.DictWriter(settingsFile, fieldnames = tag_and_instance_field_names)

        global tag
        global spinBox

        parameters = getParameterValues()

        parameter_writer.writeheader()
        parameter_writer.writerow({'team_num': parameters[0], 'neural_compute_stick': parameters[1], 'print_info': parameters[2], 'streamer': parameters[3], 'dashboard_confidence': parameters[4]})

        tag_and_instance_writer.writeheader()
        for entry in range(0, tagCount - 1):
            tag_and_instance_writer.writerow({'tag': tag[entry].get(), 'instance_number': spinBox[entry].get()})

def saveLoadingSettings():
    saveSettings("../EVS_GUI/resources/loading_parameters/")

def deleteLoadingSettings(): # TODO: Fix this thing
    os.remove("../EVS_GUI/resources/loading_parameters/EVS_setting.csv")

def loadSettings(file = None):
    # Select a directory
    if file == None:
        file = selectFile(title = "Select a parameter file to load the values from:", file_ext = ".csv")

    global tag
    global spinBox
    global raw_team_number
    global neural_compute_stick
    global print_info
    global streamer
    global dashboard_confidence
    global neural_compute_stick_checkbox
    global print_info_checkbox
    global streamer_checkbox
    global dashboard_confidence_checkbox

    # Load the settings from a .csv file
    with open(file, mode='r') as settingsFile:

        datareader = csv.reader(settingsFile, delimiter=',')
        data = []
        for row in datareader:
            data.append(row)

        for entry in range(0, 9):
            tag[entry].set(data[entry + 3][0])
            spinBox[entry].set(data[entry + 3][1])

        raw_team_number.set(data[1][0])
        
        if not neural_compute_stick.get() == (data[1][1] == "True"):
            neural_compute_stick_checkbox.toggle()

        if not print_info.get() == (data[1][2] == "True"):
            print_info_checkbox.toggle()

        if not streamer.get() == (data[1][3] == "True"):
            streamer_checkbox.toggle()

        if not dashboard_confidence.get() == (data[1][4] == "True"):
            dashboard_confidence_checkbox.toggle()



def onDirError(self):
    tk.messagebox.showerror("Error", "Could not open file")


def generateFiles():

    global tag
    global tag_list
    global instance_list
    global raw_team_number
    global neural_compute_stick
    global print_info
    global streamer
    global dashboard_confidence

    # Get tags until one is empty
    for entry in range(0, len(tag)):
        tag_entry_value = tag[entry].get()
        if not tag_entry_value == "":
            tag_list.append(tag_entry_value)
            continue
        else:
            break

    # Set the instance list to the values
    for entry in range(0, len(tag_list)):
        instance_list.append(spinBox[entry].get())

    # TODO: Create check function
    raw_team_number_val = float(raw_team_number.get())

    neural_compute_stick_val = neural_compute_stick.get()

    print_info_val = print_info.get()

    streamer_val = streamer.get()

    dashboard_confidence_val = dashboard_confidence.get()

    python_file_contents = generate_py_file.generatePythonFile(tag_list, instance_list, raw_team_number_val, neural_compute_stick_val, print_info_val, streamer_val, dashboard_confidence_val)

    selectDir(title = "Choose a directory for the output files:")
    python_file = open("app.py", mode = "w+")
    python_file.write(python_file_contents)

    print("Finished file export!")


def createImage(path, x_location, y_location, scale):
    global currentDir
    image = Image.open( currentDir + path)
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

    def set(self, int_value):
        self.spinbox.delete(0)
        self.spinbox.insert(0, int_value)

    def hide(self):
        self.spinbox.place_forget()

    def show(self):
        self.spinbox.place(x = self.spinbox.x, y = self.spinbox.y)


if __name__ == '__main__':
    main()