#Day 5 -> Typecasting in python


#Explicit typecasting  (changing a string into integer)
a= "34" 
b= 2
print("the sum is ", int(a)+ b )

x = int(3.7)                                        # Output: 3
y = int("10")                                       # Output: 10


#converts to boolean
print(bool(0))                                      # Output: False
print(bool("Hi"))                                   # Output: True



#Implicit Typecasting (python interpretor does this )

a=7  
b=3.0
print(type(a), "\t", type(b))                       #Output: <class 'int'>    <class 'float'>


c= a+b 
print(type(c))                                      #Output: <class 'float'>
