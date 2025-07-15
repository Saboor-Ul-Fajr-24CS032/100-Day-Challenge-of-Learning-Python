Day 53 ->  Class Methods as alternative constructor


when we create an object, the constructor __init__ runs to set the values. But sometimes, we want to create objects in a different way. For that, we can use class methods as alternative constructors.
Class methods use the @classmethod decorator and take cls as the first argument. This means the method belongs to the class, not to an object. Using class methods, we can create objects from strings, dictionaries, or with special default values.
So, class methods help us create objects in different, easier ways.