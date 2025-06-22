Day 41 -> Import Working

Importing in Python:
Importing in Python means bringing in code from another module or file so you can use its functions, variables, or classes in your own program.
Python has built-in modules (like math, random, datetime) and also allows you to create your own modules.
By importing, we reuse existing code instead of writing everything from scratch.


Import keyword:
This is the basic way to import a module.

import math
print(math.sqrt(16)) 

Here, we import the whole math module.
To use any function inside, we prefix it with math. (e.g., math.sqrt()).


from keyword:
This allows you to import specific parts of a module instead of the whole module.

from math import sqrt
print(sqrt(25)) 

Only the sqrt function is imported. Now you can use it directly without typing math.sqrt.
You can also import multiple things


import * (Import Everything):
This imports everything from a module without prefix.

from math import *
print(sqrt(36))  
print(pi)         

But it is not recommemd. It may overwrite existing variables.
It’s unclear where functions are coming from.


as keyword (Renaming Modules):
You can use as to give a custom name or short alias to a module or function. This helps in writing cleaner code.

import math as m


dir() function:
dir() is a built-in Python function that lists all functions, classes, and variables inside a module.


