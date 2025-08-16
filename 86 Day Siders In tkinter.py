# Day 86 -> Siders In tkinter

from tkinter import *

root= Tk()
root.geometry("655x455")

def getvalues():
    print(f"The user chosses : {myslider1.get()}")


# myslider = Scale(root, from_=0, to=100)
# myslider.pack()
Label(root,text="How many Values can we get" ). pack()
myslider1 = Scale(root, from_=0, to=100, orient="horizontal", tickinterval=50)
myslider1.set(50)
myslider1.pack()
Button(root, text="Getvalues", command = getvalues).pack()

root.mainloop()
