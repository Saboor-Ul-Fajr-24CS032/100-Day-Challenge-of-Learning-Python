# Day 39 -> read(), readlines() and other methods 


#readlines method
f= open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)



#writelines method
f=open('myfile1.txt', 'w')
lines=["line1\n",'line2\n', 'line3\n']
f.writelines(lines)
f.close()



# in the file (myfile.txt)
# i am learning python 
# line 2 
# ine 3
# yeahhhh


# in the file (myfile1.txt)
# line1
# line2
# line3
#