# Day 85 -> Message Box

from tkinter import *
import tkinter.messagebox as msg0


root= Tk()
root.geometry("655x455")

def help():
    print("I will help you. ")
    msg0.showinfo("Help", "Contact Saboor (Your Programmer) ")

def Rating():
    print("Rating :")
    value = msg0.askquestion("Was your experiance Good")
    print("value", value)
    if value=="yes":
        msg= "Rate us on appstore ."
    else :
        msg= "Tell us what went wrong"

    msg0.showinfo("Experiance", msg)

def friending():
    ans= msg0.askretrycancel("Function Name :", "Even if you love her 'Always' You Won't get her. ")
    if ans:
        print("If youu retry to live , You are gonna be Severus Snape.")

    else:
        print("You never love her before. ")    


mymenu= Menu(root)
m1= Menu(mymenu, tearoff=0)
m1.add_command(label="Use Help", command = help)
m1.add_checkbutton(label="Rate Us: ", command=Rating)
m1.add_command(label="Friending", command=friending)
mymenu.add_cascade(label="Using Help", menu= m1)
root.config(menu= mymenu)

root.mainloop()
