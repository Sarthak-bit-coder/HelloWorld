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

    if messagebox.askyesno("Question", "Do you like Python?"):
        print("Awesome! Keep coding in Python.")


button = Button(window,
                text="Click Me!",  # text on the button
                command=click
                )

button.pack()  # place the button on the window
window.mainloop()  # place window on computer screen and listen for events
