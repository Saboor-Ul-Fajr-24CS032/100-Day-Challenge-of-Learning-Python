# Day 74 -> GUI using Tkinter 


from tkinter import *

root = Tk()

#width x Height
root.geometry("768x640") 


root.minsize(512, 512)

root.maxsize(1200, 768)

var1= Label(text="Saboor is a written programmer")
var1.pack()

root.mainloop()