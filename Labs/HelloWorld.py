# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Name: Christian Piper
# Date Created: 8/28/19
# This program will print Hello World to the screen
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import tkinter

def main():
    print("Hello World")

def gui():
    gui = tkinter.Tk( screenName= 'GUI_Program',  baseName=None, )
    gui.mainloop
    gui.title('Something')

main()
gui()
