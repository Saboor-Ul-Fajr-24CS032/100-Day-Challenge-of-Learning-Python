# Day 24 -> Sets in python 

set= {2,4,2,6}
print(set)
# Output = {2,4,6}


s1= {"saboor", 32, 7.9, False, 32, 7.91 }
print(s1)
# Output {32, False, 7,91, 'saboor', 7.9} , There is no gurantee to maintain order in it . That's why they are printed like that.


empty_set = __builtins__.set()
print(type(empty_set))
# Output : <class 'set'> ,  That's how we create an empty set 


for value in s1:
    print(value)
# Output : 32
#         False
#         7.91
#         saboor
#         7.9    , Accessing the values 

