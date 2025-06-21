#Day 37 Final Keyword

def  fac1():
    try:
        var= [1, 2, 3, 4]
        var2= int(input("Enter the index : "))
        print(var[var2])
        return 1
    except:
        print("error occured")
        return 0
                                                   #In this finally will always work even when the funation returns the value
    finally:
        print("I am always executed. ")





def  fac():
    try:
        var= [1, 2, 3, 4]
        var2= int(input("Enter the index : "))
        print(var[var2])
        return 1
    except:
        print("error occured") 
        return 0                        #In this the line after return will ot be executed .  
    
    print("I will be executed. ")



fac1()
fac()