# Day 44 Local vs Global Variable


x= 7
print(x)
def sum():
    x=6
    print(F"the sum of global variable is {x} ")

sum()
print(x)

#Changing the value of global variable with the value of local variable
x1= 7
print(x1)
def sum():
    global x1 
    x1=10
    print(F"the sum of global variable is {x1} .")

sum()
print(x1)

