from tkinter import *

window = Tk()  # create a window object

x = IntVar()  # variable to hold the state of the check box (1 for checked, 0 for unchecked)


def display():
    if x.get() == 1:
        print("You checked the box!")
    else:
        print("You unchecked the box!")


check_button = Checkbutton(window,
                           text="Check Me!",  # text next to the check box
                           variable=x,  # bind the check box to the variable x
                           onvalue=1,  # value when checked
                           offvalue=0,  # value when unchecked
                           command=display,  # function to call when check box is clicked
                           font=('New Roman', 20)  # set font type and size
                           )

check_button.pack()  # place the check box on the window
window.mainloop()  # place window on computer screen and listen for events
