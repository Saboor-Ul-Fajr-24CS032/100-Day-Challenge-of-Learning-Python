# Day 77 -> Frame in Tkinter


from tkinter import * 
root = Tk()
root.geometry("655x544")

f1 = Frame(root, bg="grey", borderwidth=1, relief=SUNKEN)
f1.pack(side= LEFT, fill="y")

f2 = Frame(root,bg= "grey",  borderwidth=2, relief=SUNKEN)
f2.pack(side="top", fill="x")

l1 = Label(f1, text="Project Tkinter -Notpad", font=("Times new Roman"  ,12)  )
l1.pack()

l2 = Label(f2, text="Welcome to Notpad", font=("Helvetics"  ,18,  "bold "))
l2.pack()

root.mainloop()