from tkinter import *
from PIL import ImageTk,Image

root =Tk()
root.title('IMAGEVIEWER')

my_img2 = ImageTk.PhotoImage(Image.open("images/1.jpeg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/2.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/3.png"))
my_img5 = ImageTk.PhotoImage(Image.open("images/3b.jpeg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/4.jpeg"))

image_list = [my_img2, my_img3, my_img4, my_img5, my_img6]

mylabel2= Label(image= my_img2)
mylabel2.grid(row=0, column=0, columnspan= 3)
status = Label(root, text= "Image 1 of " +str(len(image_list)),bd=1, relief=SUNKEN, anchor=E)

#functions
def forward(image_number):
    global mylabel2
    global button_next
    global  button_back
    mylabel2.grid_forget()
    mylabel2 = Label(image= image_list[image_number-1])
    button_next = Button(root, text=">>", bg="grey", borderwidth=2, command=lambda :forward(image_number+1))
    button_back = Button(root, text= "<<", bg="grey", borderwidth=2, command=lambda :back(image_number-1))
    if image_number ==5:
        button_next = Button(root,text=">>", bg="grey", borderwidth=2, state= DISABLED)
    mylabel2.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)

    status = Label(root, text="Image " +str(image_number)+ " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=2, columnspan=3, sticky=W + E)


def back(image_number):
    global  mylabel2
    global button_next
    global button_back
    mylabel2.grid_forget()
    mylabel2 = Label(image=image_list[image_number - 1])
    button_next = Button(root, text=">>", bg="grey", borderwidth=2, command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", bg="grey", borderwidth=2, command=lambda: back(image_number - 1))

    if image_number== 1:
        button_back= Button(root, text="<<", state= DISABLED)

    mylabel2.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    #updating status bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN,
                   anchor=E)
    status.grid(row=2, column=2, columnspan=3, sticky=W + E)

# buttons
button_back = Button(root, text="<<", bg="grey", borderwidth=2, command=back, state= DISABLED)
my_exit_button = Button(root, text="CLOSE", command= root.quit, bg="#C70039", fg="white", borderwidth=2)
button_next = Button(root, text=">>", bg="grey", borderwidth=2, command=lambda :forward(2))
button_back.grid(row=1, column=0)
my_exit_button.grid(row=1, column=1)
button_next.grid(row=1, column=2)
status.grid(row=2, column=2, columnspan=3, sticky=W+E)

root.mainloop()