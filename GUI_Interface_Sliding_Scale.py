from tkinter import *

window = Tk()  # create a window object


def submit():
    print(f"Scale value: {scale.get()}")
#   print("The temperature is " + str(scale.get()) + " degrees Celsius")


scale = Scale(window,
              from_=0,  # set the minimum value of the scale
              to=100,  # set the maximum value of the scale
              # set the orientation of the scale (HORIZONTAL or VERTICAL)
              orient=VERTICAL,
              length=300,  # set the length of the scale
              width=20,  # set the width of the scale
              tickinterval=10,  # set the tick interval of the scale
              resolution=1,  # set the resolution of the scale (step size)
              # set the color of the trough (the background of the scale)
              troughcolor='#69EAFF',
              fg='#FF1C00',  # set the color of the text on the scale
              bg='#111111'   # set the background color of the window
              )
scale.set(50)  # set initial value of scale to 50

button = Button(window,
                text="Submit",
                command=submit
                )

button.pack()  # place button on window
scale.pack()  # place scale on window

window.mainloop()  # place window on computer screen and listen for events
