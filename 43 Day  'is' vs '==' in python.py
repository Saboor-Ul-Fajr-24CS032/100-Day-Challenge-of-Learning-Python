# Day 43 -> 'is' vs '==' in python


#in this both are false cause the memory location is different and value to
a=4
b="4"
print(a is b)
print(a==b) 



#the list is mutable , so python makes two different locations 
a=[1,2]
b=[1,2]
print(a is b)
print(a==b) 



#the tuple is immutable , so python only makes a single space for both of them 
a=(1,2)
b=(1,2)
print(a is b)
print(a==b) 
