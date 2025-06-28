Day 43 -> 'is' vs '==' in python



1. is Operator (Identity Comparison)
Checks whether two variables point to the same object in memory.
It does not care about the content — only whether both names refer to the exact same object.

2. == Operator (Equality Comparison)
Checks whether the values of the two objects are the same.
It compares the content element by element (for lists etc.).
It doesn’t care if they are different objects as long as their data matches.

For immutable types (like integers and strings), Python often reuses objects in memory, so is and == can both return True.