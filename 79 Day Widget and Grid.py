# Day 79 -> Widget and Grid

from tkinter import *

root= Tk()
root.geometry("655x333")


def getvalues():
    print(a_value.get())
    print(b_value.get())

a= Label(root, text= "Username")
b= Label(root, text= "Password")
a.grid()
b.grid(row=1)

a_value= StringVar()
b_value = StringVar()

a_entry= Entry(root, textvariable=a_value)
b_entry= Entry(root, textvariable= b_value)

a_entry.grid(row=0, column=1)
b_entry.grid(row= 1 , column=1)

Button(text="Submit", command=getvalues) . grid()

root.mainloop()
