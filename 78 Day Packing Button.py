# Day 78 -> Packing Button 


from tkinter import * 

root = Tk()
root.geometry("655x455")

def hello():
    print("Hello")

def name():
    print("MY name is saboor ")

F1= Frame(root, borderwidth=2, bg="grey", relief="solid")
F1.pack(side=TOP, anchor="nw", fill="x")

b1= Button(F1, fg="white", bg="black", command=hello, padx= 12, pady=9)
b1.pack(side=LEFT, padx= 7)

b2= Button(F1, fg="white", bg="black", command=name, padx= 12, pady=9)
b2.pack(side=LEFT, padx=7)

b3= Button(F1, fg="white", bg="black", padx= 12, pady=9)
b3.pack(side=LEFT, padx=10)

b4= Button(F1, fg="white", bg="black", padx= 12, pady=9)
b4.pack(side=LEFT, padx=10)

root.mainloop()
