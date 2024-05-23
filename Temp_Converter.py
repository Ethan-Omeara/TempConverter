from tkinter import *

root = Tk()

dispC = DoubleVar()
dispF = DoubleVar()

def setC(*args):
    celsius = dispC.get()
    dispF.set(round((9/5)*celsius+32, 2))

def setF(*args):
    fahrenheit = dispF.get()
    dispC.set(round((fahrenheit-32)*(5/9), 2))

dispC.trace_add("write", setC)
dispF.trace_add("write", setF)

Entry(root, textvariable=dispC).pack()
Entry(root, textvariable=dispF).pack()

root.mainloop()