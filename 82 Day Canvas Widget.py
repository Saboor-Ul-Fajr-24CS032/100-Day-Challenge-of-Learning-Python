# Day 82 -> Canvas Widget 

from tkinter  import *
root = Tk()

canvas_width= 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget= Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

can_widget.create_line(0, 200, 800, 400)

#(cordinates of top eft, cordinates of top right)
can_widget.create_rectangle(2,2, 250, 300, fill="grey")
can_widget.create_text(200, 200, text="Writing")


can_widget.create_oval(30, 5,500,250  )
root.mainloop()