from tkinter import *

window = Tk()  # create a window object

count = 0


def click_me():
    global count
    count += 1
    print(f"You clicked the button {count} times!")

# photo = PhotoImage(file="GAMES/PXL_20250530_181416321.MP.jpg")  # make sure to use .png files for images and the path is correct


button = Button(window,
                text="Click Me!",  # text on the button
                command=click_me,  # function to call when button is clicked
                activeforeground="red",  # text color when button is clicked
                activebackground="yellow"  # background color when button is clicked
                # state=DISABLED  # disable the button
                )

button.pack()  # place the button on the window

window.mainloop()  # place window on computer screen and listen for events
