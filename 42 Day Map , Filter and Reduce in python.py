# Day 42 -> Map , Filter and Reduce in python
 


#Map
def square(x):
    return x*x

print(square(2))
l=[1,2,3,4,5]

newl= map(square,l)
print(newl)
print(list(newl))





#Filter
l1= [3,4,5,6,2,7,8,1]

def filter_function(a):
    return a>=4

newl1= filter(filter_function, l1)
print(newl1)
print(list(newl1))





#Reduce -> adding all from list
from functools import reduce

l1= [3,4,5,6,2,7,8,1]
sum= reduce(lambda x,y: x+y, l1)

print(sum)