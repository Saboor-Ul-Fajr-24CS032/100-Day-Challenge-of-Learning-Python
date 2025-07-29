Day 74 -> GUI using Tkinter 


What is Tkinter:
Tkinter is Python’s built-in library for creating GUI (Graphical User Interface) applications.
It provides widgets like windows, labels, buttons, text boxes, etc.

Importing Tkinter: 
( from tkinter import * )
This imports all Tkinter classes and functions.
Now you can directly use widgets like Label, Button, Tk() without writing tkinter. each time.

Creating the Main Window:
( root = Tk()  )
Tk() initializes the main window (also called the root window).
This is where all widgets will be placed.

Functions:

geometry() :
Sets the initial size of the window when it opens.

minsize() :
Sets the minimum width and height for the window.
The user cannot shrink the window below this size.

maxsize() :
Sets the maximum width and height for the window.
The user cannot stretch the window larger than this size.

Adding a Label (Text Widget) :
Code : { var1 = Label(text="Saboor is a written programmer")
var1.pack()  }
Label() creates a text widget showing "Saboor is a written programmer".
pack() automatically positions the label inside the window (centered by default).

Running the Application: 
( root.mainloop() )
Starts the event loop which keeps the window open.
Listens for user actions (like resizing, closing, clicking).
The program will keep running until the user closes the window.
