# Day 83 -> Handling Events 


from tkinter import *

def harry(event):
    print(f"you clicked the button at {event.x}, {event.y}")

root= Tk()
root.geometry("800x400")
root.title("Events")

widget= Button(root, text= "click me ")
widget.pack()
widget.bind('<Button-1>', harry )
widget.bind('<Double-1>', quit)

root.mainloop()