# Day 19 -> Introduction to tuples


tuple1=(1,2, 56, 32, "saboor", "Saboor")
print(type(tuple1), tuple1)


#Positive indexing
print(tuple[0])
print(tuple[4])


#Negative indexing
print(tuple1[-2])


#Checking Item
if "saboor"in tuple1:
    print("saboor is present")
else:
    print("It is not present")


#Range of Index (start: end:jumpindex)
print(tuple1[2:4])
print(tuple1[1:4:2])


