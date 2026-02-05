from tkinter import *

window = Tk()  # create a window object


def add():
    print(f"You added: {entryBOX.get()}")
    listbox.insert(listbox.size(), entryBOX.get())


def submit():

    food = []
    for index in listbox.curselection():
        # get the selected items from the list box
        food.insert(index, listbox.get(index))

    print("You ordered: ")
    for item in food:  # print each item in the food list
        print(item)


def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)


listbox = Listbox(window,
                  selectmode=MULTIPLE,  # SINGLE, BROWSE, MULTIPLE, EXTENDED
                  bg="white",  # set background color
                  fg="black",  # set font color
                  width=30,  # set width of list box
                  # set height of list box (number of items to show)
                  height=10,
                  font=('New Roman', 20),  # set font type and size
                  bd=5,  # set border width
                  relief=GROOVE  # set border style
                  )

listbox.pack()  # place the list box on the window

listbox.insert(1, "PIZZA")  # insert items into the list box
listbox.insert(2, "BURGER")
listbox.insert(3, "PASTA")
listbox.insert(4, "SANDWICH")
listbox.insert(5, "FRIES")

listbox.config(height=listbox.size())  # adjust height based on number of items

entryBOX = Entry(window,
                 font=('New Roman', 20),  # set font type and size
                 fg="black",  # set font color
                 bg="white",  # set background color
                 width=30,  # set width of entry box
                 bd=5,  # set border width
                 relief=GROOVE  # set border style
                 )
entryBOX.pack()  # place the entry box on the window

submit_button = Button(window,
                       text="Submit",
                       command=submit
                       )
submit_button.pack()  # place the submit button on the window

add_button = Button(window,
                    text="Add Item",
                    command=add
                    )
add_button.pack()  # place the add button on the window

delete_button = Button(window,
                       text="Delete Item",
                       command=delete
                       )
delete_button.pack()  # place the delete button on the window

window.mainloop()  # place window on computer screen and listen for events
