from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()
    print(color)
    # get the hexadecimal color code from the selected colora
    colorHex = color[1]
    # change the background color of the window to the selected color
    window.config(bg=colorHex)


window = Tk()  # create a window

window.geometry("400x400")  # set the size of the window
button = Button(text='click me', command=click)
button.pack()  # place the button on the window

window.mainloop()  # place window on computer screen and listen for events
