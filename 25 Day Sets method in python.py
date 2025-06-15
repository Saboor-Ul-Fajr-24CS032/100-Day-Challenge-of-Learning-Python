# Day 25 -> Sets Methods in python

s1= {1,2,3 ,4}
s2= {3, 4, 5 }

#Union
print(s1.union(s2))
#Output : {1, 2, 3, 4, 5, 6}


#Updating s1 
s1.update(s2)
print(s1,  s2)
#Output : {1, 2, 3, 4, 5, 6} {3, 4, 5, 6}


#Intersection
s1= {1,2,3 ,4}
s2= {3, 4, 5 }
print(s1.intersection(s2))
#output: {3, 4}


#Intersection update
s1.intersection_update(s2)
print(s1)
#output: {3, 4}


#Symmetric difference
s1= {1,2,3 ,4}
s2= {3, 4, 5 }

s3= s1.symmetric_difference(s2)
print(s3) 
#Output: {1, 2, 5}


#Difference 
s3= s1.difference(s2)
print(s3)
#Output: {1, 2}


 #Is disjoint()
s1= {1,2,3 ,4}
s2= {3, 4, 5 }
print(s1.isdisjoint(s2))
#output: False
s3= {4,5}
s4={1,2}
print(s3.isdisjoint(s4))     #Output:True



#Is Supperset
s1= {1,2,3 ,4}
s2= {3, 4}
s3= {7,8}
print(s1.issuperset(s2))    #output:True
print(s1.issuperset(s3))    #Output:False


#Is Subset 
print(s2.issubset(s1))     #Output: True
print(s3.issubset(s1))     #Output: False


#Add
s1= {1,2,3 ,4}
s1.add(5) 
print(s1)                  #Output: {1, 2, 3, 4, 5}


#Remove
s1.remove(5)
print(s1)                  #Output: {1, 2, 3, 4}


#Pop
item = s1.pop()
print(s1)                  #Output: {2, 3, 4}
print(item)                #Output: 1


#Del
s1= {1,2,3 ,4}
del s1
#print(s1)# Because the s1 has been deleted it gives an error.


#clear
s2= {1,2,3 ,4}
s2.clear()
print(s2)                #Output:
