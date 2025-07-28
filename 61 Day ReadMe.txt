Day 61 -> Multilevel Inheritance


Multilevel Inheritance:
Multilevel inheritance occurs when a class inherits from a derived class, which itself inherits from a base class.
This creates a class chain, where the last class in the hierarchy has access to all attributes and methods from its ancestors.

Uses:
It reuses existing code.
It builds more specialized classes step by step.
It makes code organized and readable.

Things to Keep in Mind:
It can get complex with long chains.
Always use super() if possible to ensure proper initialization.
Be careful with method overriding in deep hierarchies.

