# Day 65 -> Walrus Operator 



a = True 

print(a:=False)


num= [1, 2, 3, 4]

while (n:= len(num)) >0:
    print(num.pop())


foods = list()
while( food:= input("what food do you like : ")) != "quit":
    foods.append(food)