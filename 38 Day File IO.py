# Day 38 -> File IO


#Opening a file 
f=open('38 Day ReadMe.txt', 'r')

text= f.read()
print(text)
f.close()

  


# Writing a file 

f=open('myfile.txt', 'w')
f.write("hello i am writing to file name myfile.txt and i am writing this from a python file Day 38 ")
print("done")
f.close()


#appending

f=open('myfile.txt', 'a')
f.write("\nAppending the file ")
print("done")
f.close()


with open('myfile.txt', 'a') as f :
    f.write("\ni am using with keyword")
