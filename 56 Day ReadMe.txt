Day 56 -> Dunder or Magic methods


Magic Methods:
Magic methods (also called dunder methods, short for “double underscore”) are special built-in methods
They start and end with double underscores like __init__, __len__, etc.
They allow your objects to interact with Python's built-in functions and operators, such as +, len(), print(), etc.

Common Magic Methods:

1. __init__ (self, ...)
This is the constructor.
Automatically called when you create a new object.
Used to initialize object attributes.

2. _str__(self):
Returns a user-friendly string when print(object) is used.

3. __repr__(self):
Returns a string that should ideally recreate the object if in any chance the object will be misplaced.

4. __call__(self, ...)
Makes an object callable like a function.

5. __len__(self)
You use the len() function on your object.