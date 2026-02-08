from tkinter import *


def click():
    input = text.get("1.0", END)  # get the text from the text widget
    print(input)  # print the text to the console


window = Tk()  # create a window

text = Text(window,
            height=5,
            width=30,
            bg="light yellow",
            font=("Ink Free", 16),
            padx=10,
            pady=10
            )  # create a text widget with specified properties

text.pack()  # place the text widget on the window
button = Button(window, text="Get Text", command=click)
button.pack()  # place the button on the window

window.mainloop()  # place window on computer screen and listen for events
