from tkinter import *

# widgets = GUI elements: buttons, text boxes, labels, images
# windows = containers for these elements

window = Tk()  # create a window object
window.geometry("420x420")  # set the size of the window
window.title("Sarthak's First GUI")  # set the title of the window
window.config(background="#1A94B9")  # set the background color of the window

# create photo image object:

# icon = PhotoImage(file="GAMES/PXL_20250530_181416321.MP.jpg") # make sure to use .png files for images and the path is correct
# window.iconphoto(True, icon)  # set the icon of the window

label = Label(window, text="Hello World!", font=('New Roman', 20), fg="black", bg="#054153",  # create a label widget with "Hello World!" text
              relief=RAISED,  # set the border style of the label
              bd=10,  # set the border width of the label
              padx=20,  # set the x padding of the label
              pady=20,  # set the y padding of the label
              image=None  # can add an image to the label
              )
label.pack()  # place the label on the window
# x and y coordinates can be specified in pack()

window.mainloop()  # place window on computer screen and listen for events
