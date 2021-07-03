from tkinter import *
from PIL import Image,ImageTk

root= Tk()
root.title('Creating a new Window')

def open():
    global myImage
    top = Toplevel()
    top.title('Images')
    myImage = ImageTk.PhotoImage(Image.open("images/5.jpeg"))
    myLabel = Label(top, image=myImage).pack()
    btn2= Button(top, text="CLOSE", bg="blue", fg="white", command= top.destroy).pack()

btn= Button(root, text="OPEN ON NEW WINDOW ", command=open, bg="red", fg="white").pack()



root.mainloop()