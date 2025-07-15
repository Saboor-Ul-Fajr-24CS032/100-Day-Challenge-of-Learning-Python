Day 52 -> Class Methods 


Python Class Methods:
A class method is a method bound to the class, not to an instance.
It works on the class itself, not on a single object.
Defined using the @classmethod decorator.

Why Use Python Class Methods:
It is Useful for creating factory methods that return class instances in a custom way.
It Help define alternative constructors — multiple ways to create objects with a consistent interface.
It is Good for any operation needing access to the class, not an individual object.

How to Use Python Class Methods:
Decorate the method with @classmethod.
The first parameter must be cls.

Class methods cannot directly modify the class itself.
If you need to change class-level data, use class variables.

