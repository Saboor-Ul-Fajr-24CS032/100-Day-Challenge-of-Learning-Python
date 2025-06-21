#Day 38 -> Customs Errors

var = int(input("Enter the number between 10 to 20 : "))

if(var<10 or var>20 ):
    raise ValueError("Error Ocuuried, value should be in between of 5 and 9")




#quick quiz

var1= input("Enter quit or else the program will raise an error : ")

if (var1!= "quit"):
    raise ValueError("The word is not quit. ")

print("var1")