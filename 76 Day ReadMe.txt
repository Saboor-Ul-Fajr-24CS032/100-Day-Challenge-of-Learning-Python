Day 76 -> Attributes of Label and Pack


Label(...) : Creates a Label widget to display text or images.

Inside the Label(...)(Different Functions):

text = '''...''': Multi-line text displayed in the label.
bg="lightblue": Sets the background color to light blue.
foreground="white": Sets the text color to white.
padx=40: Adds 40 pixels padding left and right inside the label.
pady=70: Adds 70 pixels padding top and bottom inside the label.
font=("Times new roman", 19, "bold"): Sets the font to Times New Roman, size 19, bold.
borderwidth=3: Sets the thickness of the border.
relief=RIDGE: Gives a 3D ridge effect around the label.

Pack Options:

side="bottom": Positions the label at the bottom of the window.
anchor="se": Anchors (aligns) the label to the south-east (bottom-right) corner.
fill="x": Expands the label horizontally to fill the window width.
padx=34, pady=50: Adds external padding around the label (outside the label’s border).

