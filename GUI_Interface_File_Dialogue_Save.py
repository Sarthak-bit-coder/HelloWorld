from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file is NONE:
        return
    fileText = text.get("1.0", END)  # get the text from the text widget
    # input = "What something here I guess: " # gets the text from the console if you want to write something to the file from the console instead of the text widget
    file.write(fileText)  # write the text to the file
    file.close()  # close the file after writing to it


window = Tk()  # create a window

button = Button(text="Save File",
                command=saveFile)
button.pack()  # place the button on the window
text = Text(window,)
text.pack()  # place the text widget on the window

window.mainloop()  # place window on computer screen and listen for events
