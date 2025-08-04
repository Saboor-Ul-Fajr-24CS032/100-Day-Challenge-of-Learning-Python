# Day 80 -> CheckButtons and Entry Widgets


from tkinter import* 
root = Tk()
root.geometry("644x344")

def getvals():
    print("It works ")

Label(root, text= "Welcome to Travels", font= "comicsansms 13 bold").grid(row=0, column=3)


name = Label(root, text= "Name :")


name.grid (row = 2 , column = 1)



namevar= StringVar
foodvar= IntVar

nameentry= Entry(root, textvariable=namevar)

nameentry.grid(row= 2 , column = 3 )

#CheckBox

foodser= Checkbutton(text="Want to prebook your meals ?",variable=foodvar )
foodser.grid(row=3 , column = 3 )

Button1= Button(text="Submit .", command= getvals ).grid(row=5 , column = 3 )

root.mainloop()
