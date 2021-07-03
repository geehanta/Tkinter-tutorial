from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog

root = Tk()
root.title('FILE DIALOG BOX')


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/Images", title="select a file",filetypes=(("Png files", ".png"), ("all files", " *.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


btn = Button(root, text= "Open image", command=open, bg="grey").pack()
root.mainloop()
