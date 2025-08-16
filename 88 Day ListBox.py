# Day 88 -> ListBox 


from tkinter import *

root= Tk()
root.geometry("544x455")
#Lists of alternatives

lbx= Listbox(root)
lbx.pack()
lbx.insert(END, "first item of a listbox")
lbx.insert(ACTIVE)


root.mainloop()
