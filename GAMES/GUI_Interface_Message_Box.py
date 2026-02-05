from tkinter import *
from tkinter import messagebox

window = Tk()  # create a window o


def click():
    # messagebox.showinfo("Information", "You clicked the button!")
    # while True:
    # messagebox.showwarning(title="Warning", message="You clicked the button!")
    # messagebox.showerror("Error", "You clicked the button!")

    # if messagebox.askokcancel("Question", "Do you want to proceed?"):
    # print("You chose to proceed.")
    # else:
    #     print("You cancelled the operation.")

    # if messagebox.askretrycancel("Question", "Do you like Python?"):
    # print("Great! Python is awesome.")

    # answer = messagebox.askquestion("Question", "Do you like Python?")
    # if answer == 'yes':
    # print("Great! Python is awesome.")
    # else:
    # print("Oh no! Give Python a chance.")

    # answer = messagebox.askyesnocancel("Question", "Do you like Python?")
    # if answer is True:
    # print("Great! Python is awesome.")
    # elif answer is False:
    # print("Oh no! Give Python a chance.")
    # else:
    # print("You cancelled the operation.")

    # can be 'warning', 'info', 'question', 'error'
    if messagebox.askyesno("Question", "Do you like Python?", icon='info'):
        print("Awesome! Keep coding in Python.")


button = Button(window,
                text="Click Me!",  # text on the button
                command=click
                )

button.pack()  # place the button on the window
window.mainloop()  # place window on computer screen and listen for events
