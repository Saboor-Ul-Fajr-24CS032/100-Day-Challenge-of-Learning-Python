Day 64 -> Creating command line utility in python


Creating a Simple Calculator Command Line Utility in Python
Command line utilities are powerful tools that allow users to interact with Python programs using terminal commands. 
The argparse module makes it easy to create such utilities. 
In this example, we build a simple calculator that performs basic operations like addition, subtraction, multiplication, and division.

Overview
The utility accepts three inputs: two numbers and an operation type. Based on the operation (addition, subtraction, multiplication, or division). 
It performs the calculation and returns the result. The sys module is used to output the result to the console.

Command Line Arguments
The calculator accepts:
A first number (default value: 1.0)
A second number (default value: 5.0)
An operation name like add, sub, mul, or divide (default is add)
All arguments are passed with -- prefixes and are optional. If the user doesn’t provide them, default values are used.


Workflow
When the script runs, it checks the provided operation. Based on that, it performs the corresponding calculation between the two numbers. 
The result is then printed to the terminal using sys.stdout.write, after converting the result into a string to avoid type errors.

