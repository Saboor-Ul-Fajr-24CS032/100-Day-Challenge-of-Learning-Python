Day 45 -> Constructors in python



What is a Constructor:
A constructor is a special method in a class.
It runs automatically when you create an object.
Its main job is to initialize (set) the class’s data members (variables).
In Python, the constructor method is always named __init__.


Syntax:
def __init__(self):
    # initialize variables here

__init__ is reserved in Python as the constructor’s name.
self refers to the object being created.


Types of Constructors:

1. Default Constructor:
Takes only self as a parameter.
Doesn’t need extra input from the user.

2. Parameterized Constructor:
Takes extra arguments besides self.
These arguments help set values when creating an object.

In the last Constructors cannot return any value except None.
They just prepare the object with initial data.