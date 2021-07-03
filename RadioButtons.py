from  tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title('Radiobuttons')



TOPPINGS = [
    ("Pepperoni","Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]
pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()


#radiobuttons
#Radiobutton(frame2, text=("Option 1"), variable =r, value=1, command= lambda:clicked(r.get())).pack()
#Radiobutton(frame2, text=("Option 2"), variable =r, value=2,  command= lambda:clicked(r.get())).pack()
#labels
mylabel = Label(root, text=pizza.get())
mylabel.pack()

#buttons
b= Button(root,text="Choose", command=lambda: clicked(pizza.get()))
b.pack()


exit_button= Button(root,text="CLOSE", bg="red", fg="white", command= root.quit)
exit_button.pack()



root.mainloop()


