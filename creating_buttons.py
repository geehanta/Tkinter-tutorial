from tkinter import *

root = Tk()

def myClick():
    myLabel= Label(root, text="clicked!!")
    myLabel.pack()

myButton = Button(root, text ="Click me!",  padx=50, pady= 20, command=myClick)
myButton.pack()
root.mainloop()