# Day 75 -> Displaying Images Using Labels

from tkinter import * 
from PIL import Image, ImageTk

root = Tk()

root.geometry("2048x1024")
# photo = PhotoImage(file="1.jpg")

#for jpg images 
image0 = Image.open("2.jpg")
photo = ImageTk.PhotoImage(image0)



label1 = Label(image=photo)
label1.pack()


root.mainloop()