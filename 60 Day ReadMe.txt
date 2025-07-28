Day 60 -> Multiple Inheritance 


Multiple Inheritance:
Multiple inheritance allows a class to inherit from more than one parent class.
This is useful when a class needs to combine functionalities from different sources.
It’s powerful but must be used carefully, especially with overlapping method names.

MRO():
Python uses MRO (Method Resolution Order) to decide which method or attribute to call if there’s a conflict.
You can check the MRO using:
print(class_name.__mro__)