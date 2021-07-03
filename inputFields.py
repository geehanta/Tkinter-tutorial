from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="grey", borderwidth=3)
e.pack()
e.get()
e.insert(0, "Enter your name")


def myClick():
    myLabel = Label(root, text="Hello " +e.get())
    myLabel.pack()


nameButton = Button(root, text="Enter your name", command=myClick, bg="orange", fg="white")
nameButton.pack()

# functions


root.mainloop()
