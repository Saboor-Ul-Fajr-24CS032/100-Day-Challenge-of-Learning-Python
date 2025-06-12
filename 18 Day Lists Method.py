# Day 18 -> Lists Methods


#sort 
a = [1, 34, 23, 54, 21, 12, 99, 3]
a.sort()
print(a)                                    #Ascending Order

a.sort(reverse=True)
print(a)                                    #Descending Order



#reverse
b = [1, 34, 23, 54, 21, 12, 99, 3]
b.reverse()
print(b)



#Index
c = [1, 34, 23, 54, 21, 12, 99, 3]
print(c.index(54))



#Count
d = [1, 3, 3, 54, 21, 12, 99, 3]
print(d.count(3))



#Copy
e=d.copy()
print(e)



#Append
f = [1, 34, 23, 54, 21, 12, 99, 3]
f.append(100)
print(f)



#Insert
g = [1, 34, 23, 54, 21, 12, 99, 3]
g.insert(0, "hehehe")
print(g)



#Extend
h = [1, 34, 23, 54, 21, 12, 99, 3]
i= ["heheheh", "Nooooooo", "yepppppppp"]
h.extend(i)
print(h)



#Concatenating two lists
j = [1, 34, 23, 54, 21, 12, 99, 3]
k= ["heheheh", "Nooooooo", "yepppppppp"]
print(j+k)

