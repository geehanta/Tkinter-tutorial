from tkinter import *

root = Tk()
#creating widget
myLabel1 = Label(root, text="Hello there!")
myLabel2 = Label(root, text="Welcome to Wakanda!")
myLabel3 = Label(root, text="Whats your name?!")
#pushing onto screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=0)

root.mainloop()
