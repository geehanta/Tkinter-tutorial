from tkinter import  *

root = Tk()
root.title ('Checkboxes')
root.geometry("400x400")

var = IntVar()

chckbox= Checkbutton(root, text="Check", variable=var)
chckbox.deselect()
chckbox.pack()
def show():
    lbl = Label(root, text=var.get())
    if var.get() == 1:
        lbl1 = Label(root, text="Its CHECKED!!").pack()
    elif var.get()==0:
        lbl2 = Label(root, text="Its  Not CHECKED!!").pack()


myBtn = Button(root, text= "Show selection", command=show).pack()







root.mainloop()