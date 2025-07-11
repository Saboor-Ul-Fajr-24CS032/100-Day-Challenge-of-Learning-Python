50 -> Static Methods


Static methods in Python are methods that belong to the class itself, not to any instance. 
They are defined using the @staticmethod decorator and do not use self since they don’t access or modify class or instance data.

They Called directly on the class, not on its objects.
They Often used for utility functions that logically belong to the class but don’t need instance data.
They Help organize related functions under a class namespace.