# Day 89 -> ScrollBar

from tkinter import *
root= Tk()
root.geometry("544x455")


scrollbar= Scrollbar(root)
scrollbar.pack(side= RIGHT, fill=Y)
listbox1= Listbox(root, yscrollcommand=scrollbar.set)
for i in range(300):
    listbox1.insert(END, f"item({i})")


listbox1.pack(fill= "both")
scrollbar.config(command=listbox1.yview)

root.mainloop()