# Day 72 -> Multithreading in python


import threading
from concurrent.futures import ThreadPoolExecutor
import time 

def func(sec):
    print(f"Sleeping for {sec} seconds. ")
    time.sleep(sec)
    return sec

def main():
    time1= time.perf_counter()
    
    #Normal Code
    # func(5)
    # func(3)
    # func(8)


    #code using threading 
    t1= threading.Thread(target=func, args=[5])
    t2= threading.Thread(target=func, args=[3])
    t3= threading.Thread(target=func, args=[8])

    t1.start()
    t2.start()
    t3.start()

# if didn't do this , it will run on background 
    t1.join()
    t2.join()
    t3.join()

    time2= time.perf_counter()
    print(time2-time1)


def pooling():
    with ThreadPoolExecutor() as executor:
        # future1= executor.submit(func, 5)
        # future2= executor.submit(func, 3)
        # future3= executor.submit(func, 8)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        
        h= [5, 3, 8, 10]
        result= executor.map(func, h)
        for res in result:
            print(res)

pooling()