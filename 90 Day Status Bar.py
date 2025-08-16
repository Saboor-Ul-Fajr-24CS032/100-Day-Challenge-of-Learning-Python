# Day 90 -> Status Bar 

from tkinter import*
root= Tk()
root.geometry("544x455")

def Upload():
    statusvar.set("Busy")
    sbar.update()
    import time
    time.sleep(3) 
    statusvar.set("Ready now")



statusvar= StringVar()
statusvar.set("Ready")
sbar= Label(root, textvariable=statusvar, relief=SUNKEN, anchor= "w")
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="upload", command=Upload).pack()



root.mainloop()