Day 49 -> Access Modifiers 


Definition:
Access specifiers (or modifiers) in Python define how class variables and methods can be accessed from outside the class. 
They help control data visibility and support encapsulation, especially when using inheritance.

Types of Access Specifiers in Python:

1. Public:
Default in Python.
Accessible from anywhere (inside or outside the class).

2. Private:
Indicated by prefixing the name with double underscore __.
Accessible only within the class (name mangling makes outside access tricky).

3. Protected:
Indicated by prefixing with single underscore _.
Should be accessed only within the class and its subclasses (by convention).

Name Mangling:
Python internally changes the name of private variables to prevent accidental access. For example, __var becomes _ClassName__var.

