# Column is the size of the largest item in the column. Row is the size of the largest item in the row. Grid geometry manager is used to place widgets in a grid format. It is used to place widgets in a specific row and column. It is also used to span widgets across multiple rows and columns.
from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)
# First 4 and x and y corrdinates for start and end
canvas.create_line(0, 0, 500, 500, fill="Blue")
canvas.create_rectangle(50, 50, 250, 250, fill="Red")
canvas.create_polygon(250, 0, 500, 0, 500, 500, outline="Black")
# Works by giving space to work with canvas
canvas.create_arc(0, 0, 500, 500, fill="Green", start=180,
                  )  # flips using angle rotation
canvas.create_oval(180, 180, 390, 390, fill="Cyan")
canvas.pack()

window.mainloop()
