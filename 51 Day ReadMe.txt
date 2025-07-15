Day 51 -> Instance Variable vs Class Variable


Class Variables:

Defined at the class level, outside any method.
It shared by all instances of the class.
Can be accessed using ClassName.variable or self.__class__.variable.
It used for data common to every object, like a counter.

Instance Variables:

Defined inside methods, usually inside __init__.
It has unique for each object created from the class.
Can be accessed using self.variable.
it used for data specific to each object, like name or age.


