#Day 11 -> Match Case

var= int(input("Enter the number: "))

match var:
    case 0:
        print("it is zero")
    case 100:
        print("the value is 100")
    case _ if var >0:
        print("the value is positive ")
    case _ if var<0:
        print("The number is negative")
    case _ :
        print("Default")
        