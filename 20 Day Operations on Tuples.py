# Day 20 Operations on Tuples 


# Manipulating Tuple 

var1= (1, 2, 32, 56, "saboor", "Saboor")
temp= list(var1)
temp.append("noooooo")
temp.pop(1)
var1= tuple(temp)
print(var1)
var1= (1, 32, 56, 'saboor', 'Saboor', 'noooooo')

#Count
var2= var1.count(32)
print(var2)

#index
print(var1[2])                    # shows what is on index 2 

temp= var1.index("saboor")
print(temp)                       #shows on what index saboor is



