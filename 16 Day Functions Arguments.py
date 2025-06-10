# Day 16 -> Functions Arguments 



#Deafult: 
def sum(a, b=3, c=1):
    print("the sem of the numbers is ", a+b+c)

sum(2, )                                         #Output: 6
sum(2, 5, 5)                                     #Output: 12 
sum(6, b=9)                                      #Output: 16



#Keyword Arguments
def sum1(a, b, c):
    print("The sum is ", a+b -c)

sum1(3, 6, 1)                                    #Output: 8
sum1(c=1,a=3, b=6 )                              #Output: 8 



#Variable Length Arguments
def sum2(*number):
    print("Sum is ", number[0]+number[1]+ number[2])

sum2(1, 2, 3)                                     #Output: 6

def show (**number):
    print("The numbers are: ",number["a"], number["b"], number["c"])

show(b=7, c=3, a=11)                              #Output:  11 7 3


#Reurn Statement
def show1(**number):
    return "The numbers are: ",number["a"], number["b"], number["c"]

print(show1(a=3, c=9, b=7))                      #Output: ('The numbers are: ', 3, 7, 9)

