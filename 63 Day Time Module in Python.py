# Day 63 -> Time Module in Python

import time 


def usingfor():
    for i in range(5000):
        print(i)

def usingwhile():
    i=0
    while i <5000:
        i=i+1
        print(i)

init= time.time()
usingfor()
t1= time.time() -init
init11= time.time()
usingwhile()
t2= time.time() - init11
print(t1)
print(t2)



#time sleep
print("heyyy")
time.sleep(4)
print("writing again after 4 seconds")


#strf time 
t= time.localtime()
formated_time= time.strftime("%Y-%m-%D %H:%M:%S", t)
print(formated_time)