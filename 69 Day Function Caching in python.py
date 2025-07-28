# Day 69 -> Function Caching in python


from functools import  lru_cache
import time 

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(6)
    return n*5 + 3

print(fx(4))
print("4 is completed")
print(fx(41))
print("41 is completed")
print(fx(9))
print("9 is completed")


#for 4, 41, 9 the computation will not be done again and it will take the thing from cache created .
print(fx(4))
print("4 is completed")
print(fx(41))
print("41 is completed")
print(fx(9))
print("9 is completed")

print(fx(56))
print("56 is completed")