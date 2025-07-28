Day 68 -> Generators in python


Generators:
Generators are special functions in Python that return values one at a time using the yield keyword.
They don’t return all values at once like lists, but give one value each time you ask for it.

Create a Generator:
Use yield instead of return in a function.
Calling the function doesn’t run it immediately—it returns a generator object.

Using a Generator:
Use next() to get each value one by one.
Or can also use a for loop to get all values.

Why Use Generators:
It is memory efficient. It does not store all values at once.
It is fast – especially good for large or infinite data.
It is lazy execution – only runs when needed.