#Day 29 -> Exception Handling


a= input("Enter the number ")

try:
    print(f"the sum of {a} with 2 is ", int(a)+ 2)
except Exception as e:
    print(e)


print("last line ")



a= input("Enter the number ")

try:
    print(f"the sum of {a} with 2 is ", int(a)+ 2)
except:
    print("Invalid Input4")


print("last line ")



try:
    num= int(input("enter a number"))
    a=[4,5,6]
    print(a[num])
except ValueError:
    print("Number is not integer")
except IndexError:
    print("Index out of bound")
