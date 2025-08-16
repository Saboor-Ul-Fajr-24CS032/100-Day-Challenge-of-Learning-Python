Day 84 -> Menus and Submenus



Menu in Tkinter:
A Menu is a drop-down list that appears in the window's title bar.
It provides the user with commands like File, Edit, View, etc.
Menus are created using the Menu() widget and attached to the window with .config(menu=...).

Submenu in Tkinter:
A Submenu is a menu within a menu—used for grouping related commands.
It is created using another Menu() and added using .add_cascade(label=..., menu=...).
