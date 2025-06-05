# Day 14 -> Break and Continue

#Continue
for i in range (11):
    if((i+1)%5==0):
        print("Skiping only this iteration")
        continue
    print(f"{1+i} is the number")




#Break
for i in range (11):
    if((i+1)%5==0):
        print("Skiping all the iteration")
        break
    print(f"{1+i} is the number")

