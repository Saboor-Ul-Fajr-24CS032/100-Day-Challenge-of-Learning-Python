Day 44 Local vs Global Variable 


Global Variable:
A global variable is a variable that is defined outside any function. It is accessible throughout the whole program, in all functions (unless shadowed by a local variable with the same name).

Local Variable:
A local variable is declared inside a function and can only be used within that function. It exists temporarily while the function runs, and disappears when the function finishes.

Sometimes, you may want to modify the global variable inside a function.
To do this, you use the global keyword inside the function. It tells Python that you want to use the variable from the global scope, not create a new local one.
