from tkinter import *


def openFile():
    print("You clicked open file")


def saveFile():
    print("You clicked save file")


def cut():
    print("You clicked cut")


def copy():
    print("You clicked copy")


def paste():
    print("You clicked paste")


window = Tk()  # create a window

menuBar = Menu(window)  # create a menu bar
window.config(menu=menuBar)  # set the menu bar for the window

fileMenu = Menu(menuBar, tearoff=0)  # create a file menu
# add the file menu to the menu bar
menuBar.add_cascade(label="File", menu=fileMenu)
# add a "New" command to the file menu
fileMenu.add_command(label="Open", command=openFile)
# add a "Save" command to the file menu
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator()  # add a separator line to the file menu
# add a "Close" command to the file menu
fileMenu.add_command(label="Close", command=quit)

editMenu = Menu(menuBar, tearoff=0)  # create a file menu
menuBar.add_cascade(label="Edit", menu=editMenu)
# add a "New" command to the file menu
editMenu.add_command(label="Cut", command=cut)
# add a "Save" command to the file menu
editMenu.add_command(label="Copy", command=copy)
editMenu.add_separator()  # add a separator line to the file menu
# add a "Close" command to the file menu
editMenu.add_command(label="Paste", command=paste)

window.mainloop()  # place window on computer screen and listen for events
