#Day 10 If-else 

a= 100
b=200

#if-else
if(b>a):
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is bgreater than {a}")



#elif
c= int(input("enter a number : "))
if(c<0):
    print("Number is negative")
elif(c==0):
    print("number is equal to zero")
else:
    print("number is positive")



#nested if-else
if(c>0):
    if(c<10):
        print("the number is less then 10")
    else:
        print("The number is greater then 10")
else:
    print("the number is not positive ")