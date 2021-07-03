from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Messageboxes!')

frame= LabelFrame(root, padx=200, pady=200, bg="grey").grid(row=0, column=0)
#showinfo, showwarning, showerror, askquestion,askokcancel,askyesno
def showInfo():
    messagebox.showinfo("This is a PopUp","This is an informative Popup!!")

Button(frame, text="POPUP", command=showInfo, bg="blue").grid(row=0,column=0)

def showWarning():
    messagebox.showwarning("This is a PopUp","This is an warning Popup!!")
    Button(frame, text="POPUP", command=showWarning, bg="red").grid(row=0,column=1)

def showError():
    messagebox.showinfo("This is a PopUp","This is an error Popup!!")
Button(frame, text="POPUP", command=showError, bg="yellow").grid(row=0,column=2)

def askQuestion():
    messagebox.showinfo("This is a PopUp","This is a ask question popup!!")
Button(frame, text="POPUP", command=askQuestion, bg="green",padx=30,pady=20).grid(row=0,column=3)

def askokcancel():
    response= messagebox.showinfo("This is a PopUp","This is a askokcancel popup!!")
    Label(frame, text=response).grid(row=0,column=3)
    if response == "ok":
        Label(frame, text="You clicked ok").grid(row=0, column=3)
Button(frame, text="POPUP", command=askokcancel, bg="orange").grid(row=0,column=5)














root.mainloop()