from tkinter import *
from tkinter import ttk

window = Tk()  # create a window

notebook = ttk.Notebook(window)  # create a notebook widget1

tab = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab, text="Tab 1")  # add the first tab to the notebook
notebook.add(tab2, text="Tab 2")  # add the second tab to the notebook

# place the notebook on the window and make it expand to fill the available space
notebook.pack(expand=True, fill="both")

Label(tab, text="This is tab 1", font=(
    "Arial", 20), height=50, width=25).pack()
Label(tab2, text="This is tab 2", font=(
    "Arial", 20), height=50, width=25).pack()

window.mainloop()  # place window on computer screen and listen for events
