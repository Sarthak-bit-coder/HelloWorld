# Column is the size of the largest item in the column. Row is the size of the largest item in the row. Grid geometry manager is used to place widgets in a grid format. It is used to place widgets in a specific row and column. It is also used to span widgets across multiple rows and columns.
from tkinter import *
from tkinter.ttk import *
import time


def start():
    GB = 10
    download = 0
    speed = 1
    while (download < GB):
        time.sleep(0.05)
        bar['value'] += (speed/GB)*100
        download += speed
        percent.set(str((download/GB)*100)+"%")
        text.set(str(download)+"/"+str(GB))
        window.update_idletasks()


window = Tk()  # create a window

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
TaskLabel = Label(window, textvariable=text).pack()

button = Button(window, text=("download"), command=start).pack()

window.mainloop()  # place window on computer screen and listen for events
