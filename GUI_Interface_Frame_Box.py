# TopLevel() = a widget that is used to create a separate window container. Creates a new window on top of the main window that can be used to display additional information or to create a new interface for the user.
from tkinter import *

def create_window():
    new_window = Tk() # create a new window that is not dependent on the main window

    old_window.destroy()  # close the old window

old_window = Tk()  # create a window

Button(old_window, text = "Create new window", command = create_window).pack()  # place the button on the window

old_window.mainloop()  # place window on computer screen and listen for events