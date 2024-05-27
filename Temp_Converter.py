from tkinter import *
import json
db = './temperature.json'

root = Tk()
root.title("Temperature Converter")

with open(db, 'r') as file:
    temp_history = json.loads(file.read())

dispC = StringVar(name="C")
dispF = StringVar(name="F")

ignoreCommand = False
def updateTemp(var, index, mode):
    global ignoreCommand
    if ignoreCommand:
        ignoreCommand = False
        return
    ignoreCommand = True
    
    if var == "C":
        try:
            celsius = float(dispC.get())
            dispF.set(round((9/5)*celsius+32, 2))
        except:
            print("Invalid Celsius, setting blank")
            dispF.set("")
    elif var == "F":
        try:
            fahrenheit = float(dispF.get())
            dispC.set(round((fahrenheit-32)*(5/9), 2))
        except:
            print("Invalid Fahrenheit, setting blank")
            dispC.set("")

def save_temp():
    c = round(float(dispC.get()), 2)
    f = round(float(dispF.get()), 2)

    temp_history.append([c, f])
    with open(db, 'w') as file:
        file.write(json.dumps(temp_history))

dispC.trace_add("write", updateTemp)
dispF.trace_add("write", updateTemp)

Label(root, text="Celsius:", width=20).grid(row=0, column=0)
Label(root, text="Fahrenheit:", width=20).grid(row=0, column=1)

Entry(root, textvariable=dispC).grid(row=1, column=0)
Entry(root, textvariable=dispF).grid(row=1, column=1)

Button(root, text="Save", width=10, command=save_temp).grid(row=2, column=0)

root.mainloop()