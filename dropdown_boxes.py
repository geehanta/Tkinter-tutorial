from tkinter import *

root = Tk()
root.title('Drop down boxes')
root.geometry("400x400")


def show():
    lbl = Label(root, text=clicked.get()).grid(row=1, column=0)
    if clicked.get() != "Monday":
        drop2 = OptionMenu(root, var, "Morning hours", "Evening hours")
        drop2.grid(row=0, column=3)


days = ["Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"]
var= StringVar
clicked = StringVar()
clicked.set(days[0])
lbl = Label(root, text="Pick A Day")
lbl.grid(row=0, column=0)
drop = OptionMenu(root, clicked, *days)
drop.grid(row=0, column=1)

btn = Button(root, text="Choose", command=show, bg="orange", fg="white").grid(row=0, column=2)

root.mainloop()
