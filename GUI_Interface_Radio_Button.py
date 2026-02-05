from tkinter import *

# radio button = similar to check button, but only one option can be selected at a time

food = ["Pizza", "Hamburger", "Hotdog"]


def order():
    if x.get() == 0:
        print("You ordered Pizza!")
    elif x.get() == 1:
        print("You ordered Hamburger!")
    elif x.get() == 2:
        print("You ordered Hotdog!")
    else:
        print("Please select a food item!")


window = Tk()  # create a window object

x = IntVar()  # variable to hold the state of the radio buttons

# can add photos to radio buttons similar to check buttons
# foodInages = [# Make a list]

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               # text next to the radio button
                               text=food[index],
                               variable=x,  # bind the radio button to the variable x
                               value=index,  # value when this radio button is selected
                               padx=25,  # set the x padding of the radio button
                               pady=10,  # set the y padding of the radio button
                               # images = foodImages[index] # add image to radio button for the certain food index
                               # compound = 'left' # position of the text relative to the image
                               # indicatoron = 0 # makes the radio button look like a regular button
                               # width = 100 # set width of the radio button
                               command=order  # function to call when radio button is selected
                               )
    radio_button.pack(anchor=W)  # place the radio button on the window

window.mainloop()  # place window on computer screen and listen for events
