from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Images!')
my_img = ImageTk.PhotoImage(Image.open("images/1.jpeg"))
my_label = Label(image=my_img)
my_label.pack()
my_button = Button(root, text="CLOSE", command= root.quit, bg="red", fg="white")
my_button.pack()
root.mainloop()
