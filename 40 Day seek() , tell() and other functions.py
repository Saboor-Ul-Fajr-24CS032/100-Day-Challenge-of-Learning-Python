# Day 40 -> seek() , tell() and other functions 


#seek() function
with open('file.txt',"r") as f:
    print(type(f))


    f.seek(10)                        #starting from index 10 
    data = f.read(5)                  #after starting only prints 5 characters
    data1= f.read()                   #in this all the values will not print, the value after the read(5) are coming they will only be printed 
    print(data)
    print(data1)



#tell()funcction 
with open('file.txt',"r") as f:
    print(type(f))

    f.seek(10)

    print(f.tell())                    #returns the currenet position



with open('sample.txt', 'w') as f :
    f.write("Saboor is writing")
    f.truncate(5)                       #start from 1 

with open('sample.txt', 'r')as f :
    print(f.read())
    


# in file (file.txt)
#heyy , i am 4 word and checking what the python will do 

# in file (sample.txt)
#Saboo