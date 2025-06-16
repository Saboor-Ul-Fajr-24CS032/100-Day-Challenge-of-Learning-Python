#Day 28 -> For loop with else

for i in range(4):
    print(i, "in loop")
else:
    print("out of loop")

#empty list
for i in []:
      print(i, "in loop")
else:
    print("out of loop")


#with break
for i in range(4):
     print(i)
     if i ==0:
          break

else:
     print("sorry")


#while with break
i=0
while i<7:
     print(i)
     i=i+1
     if i == 4:
          break
else:
     print("sorry")

     