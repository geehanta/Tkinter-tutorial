from tkinter import *

root = Tk()
root.title('SLIDERS')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=100)
vertical.pack()
horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL)
horizontal.pack()


def Slide():
    my_label = Label(root, text=horizontal.get()).pack()


my_btn = Button(root, text="Click", command=Slide, bg="grey").pack()

root.mainloop()
