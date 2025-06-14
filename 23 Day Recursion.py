# Day 23 -> Recursion 

#Facctorial
def fact(a):
    if(a== 0 or a==1):
        return 1
    else:
        return a* fact(a-1)
    

print(fact(5))


#Fibonacci Sequence 

def seq(n):
    if n <= 1:
        return n
    else:
        return seq(n-1) + seq(n-2)
    
    

n= int(input("Enter how many numbers of fibonacci sequence you wanna see "))

for i in range(n):
    print(seq(i), " ")

