# Day 87 -> Creating RadioButtons

from tkinter import*
import tkinter.messagebox as tsmg
root= Tk()
root.geometry("544x455")
root.title("My TItle.....")

def order():
    tsmg.showinfo("order received",  f"We ave received oreder no. {var.get()} in food ordering. ")

var = IntVar()
var.set(9)
Label(root, text="What would you like to have?", justify=LEFT, font="lucide, 18 bold", padx=14).pack()
radio= Radiobutton(root, text="Biryani", padx=14, variable=var, value=1).pack( anchor="w")
radio= Radiobutton(root, text="karahi", padx=14, variable=var, value=2).pack( anchor="w")
radio= Radiobutton(root, text="gajar ka halwa", padx=14, variable=var, value=3).pack( anchor="w")
radio= Radiobutton(root, text="kheer", padx=14, variable=var, value=4).pack( anchor="w")

Button(root, text="Submit your order", padx=30, pady=100, command=order).pack()


root.mainloop()