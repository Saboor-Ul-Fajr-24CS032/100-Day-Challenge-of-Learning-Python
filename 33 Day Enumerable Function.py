# Day 40 -> Enumertae Function


#normally
index=0
var= [ 1, 2, 3, 4, 5, 6,9, 10 ]
for i in var:
    print(i)
    if(index== 7):
        print("yeahhhh")
    index+=1


#enumertae function
var1= [ 1, 2, 3, 4, 5, 6,9, 10 ]
for index , i in enumerate(var1):
    print(i)
    print(index)
    if(index== 6):
        print("yeahhhh")
    index+=1


#enumertae function with different starting index
var2= [ 1, 2, 3, 4, 5, 6,9, 10 ]
for index , i in enumerate(var2, start=2):
    print(i)
    print(index)
    if(index== 6):
        print("yeahhhh")
    index+=1


