from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Frames')

frame = LabelFrame(root, text="First frame", padx=50, pady=50)
frame.pack(padx=100, pady=100)

button_b = Button(frame, text="click me", bg="red", fg="white")
button_c = Button(frame, text="click me too", bg="red", fg="white")
button_b.grid(row=0, column=0)
button_c.grid(row=1, column=1)






root.mainloop()