Day 75 -> Displaying Images Using Labels


What is Tkinter Label Image Display:
Tkinter allows displaying images using the Label widget. 
For .jpg files, Pillow (PIL) is used to load and convert images into a compatible format.

Using the tkinter and PIL Modules:
Import tkinter and Image, ImageTk from PIL for handling and displaying .jpg images.

Opening and Converting Image:
Use Image.open() to load the image and ImageTk.PhotoImage() to convert it for Tkinter.

Displaying the Image in a Label:
Create a Label with the image and use .pack() to show it. Store the image reference to avoid garbage collection.
