# Day 84 -> Menus and Submenus


from tkinter import* 
root= Tk()
root.geometry("733x566")
root.title("84 Day ")

def func():
    print("Printing")

#for little text on top to perform task 
# mymenu= Menu(root)
# mymenu.add_command(Label="File", command= func)
# mymenu.add_command(Label=="Exit", command = quit)
# root.config()

my2menu= Menu(root)
m1= Menu(my2menu)
m1.add_command(label="Done", command=func)
m1.add_command(label="Exit", command = quit)
my2menu.add_cascade(label="File", menu= m1)
root.config(menu=my2menu)

root.mainloop()