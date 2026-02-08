# Column is the size of the largest item in the column. Row is the size of the largest item in the row. Grid geometry manager is used to place widgets in a grid format. It is used to place widgets in a specific row and column. It is also used to span widgets across multiple rows and columns. 
from tkinter import *

window = Tk()  # create a window
window.geometry("400x400")  # set the size of the window

firstNameLabel = (Label(window, text="First Name:")).grid(
    row=0, column=0)  # create a label for the first name
# create an entry widget for the first name
firstNameEntry = (Entry(window)).grid(row=0, column=1)

lastNameLabel = (Label(window, text="Last Name:")).grid(
    row=1, column=0)  # create a label for the last name
# create an entry widget for the last name
lastNameEntry = (Entry(window)).grid(row=1, column=1)

emailNameLabel = (Label(window, text="Email:")).grid(
    row=2, column=0)  # create a label for the email name
# create an entry widget for the email name
emailNameEntry = (Entry(window)).grid(row=2, column=1)

submitButton = (Button(window, text="Submit")).grid(
    # colspan = 2 means that the button will span across 2 columns
    row=3, column=0, columnspan=2)

window.mainloop()  # place window on computer screen and listen for events
