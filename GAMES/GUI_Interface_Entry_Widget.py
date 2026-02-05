from tkinter import *

# enntry widget = single line text box for user input


def submit():
    username = entry.get()
    print("Hello, " + username)
    # entry.config(state=DISABLED)  # disable the entry box after submission


def delete():
    entry.delete(0, END)  # delete from index 0 to the end


def backspace():
    entry.delete(len(entry.get())-1, END)  # delete last character


window = Tk()  # create a window object

entry = Entry(window,
              font=('New Roman', 20),  # set font type and size
              fg="black",  # set font color
              bg="white",  # set background color
              # show="*",  # show="*" will hide the text input (for passwords)
              width=30,  # set width of entry box
              bd=5,  # set border width
              relief=GROOVE  # set border style
              )
# entry.insert(0,"Enter your name here...") # insert default text in entry box

entry.pack(side=LEFT)  # place the entry box on the window

submit_button = Button(window,
                       text="Submit",
                       command=submit
                       )

delete_button = Button(window,
                       text="Delete",
                       command=delete
                       )

backspace_button = Button(window,
                          text="Backspace",
                          command=backspace
                          )

submit_button.pack(side=RIGHT)  # place the submit button on the window
delete_button.pack(side=RIGHT)  # place the delete button on the window
backspace_button.pack(side=RIGHT)  # place the backspace button on the window

window.mainloop()  # place window on computer screen and listen for events
