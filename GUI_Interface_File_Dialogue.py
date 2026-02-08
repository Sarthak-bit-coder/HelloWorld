from tkinter import *
from tkinter import filedialog

window = Tk()  # create a window


def OpenFile():
    filepath = filedialog.askopenfilename(  # initialdir = "" # set the initial directory for the file dialog
        # specify the file types that can be selected in the file dialog
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    file = open(filepath, 'r')  # open the selected file in read mode
    print(file.read())  # read the contents of the file and print it to the console
    file.close()  # close the file after reading it


button = Button(text="Open File",
                command=OpenFile)

window.mainloop()  # place window on computer screen and listen for events
