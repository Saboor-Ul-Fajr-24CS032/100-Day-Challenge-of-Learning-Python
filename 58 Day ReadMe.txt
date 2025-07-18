Day 58 -> Overloading Operators


What is Operator Overloading:
Operator overloading allows you to *define how operators (+, -, , ==, etc.) work with objects of your own classes.
Python lets you customize these operations by using special methods (dunder methods like __add__, __eq__, etc.).
It makes code more natural and readable.
Instead of writing p1.add(p2), We can simply write p1 + p2.

Common Operators and Their Methods:
+ → __add__

- → __sub__

* → __mul__

/ → __truediv__

== → __eq__

< → __lt__, > → __gt__
