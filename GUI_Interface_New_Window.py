from tkinter import *

window = Tk()  # create a window

# create a frame with specified properties
frame = Frame(window, bg="blue", padx=10, pady=10)
frame.pack()  # place the frame on the window

Button(frame, text="W", font=("Comic Sans MS", 20), fg="red", bg="yellow",
       padx=10, pady=10).pack(side=TOP)  # place the button on the window
Button(frame, text="A", font=("Comic Sans MS", 20), fg="red", bg="yellow",
       padx=10, pady=10).pack(side=LEFT)  # place the button on the window
Button(frame, text="S", font=("Comic Sans MS", 20), fg="red", bg="yellow",
       padx=10, pady=10).pack(side=LEFT)  # place the button on the window
Button(frame, text="D", font=("Comic Sans MS", 20), fg="red", bg="yellow",
       padx=10, pady=10).pack(side=LEFT)  # place the button on the window


window.mainloop()  # place window on computer screen and listen for events
