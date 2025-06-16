#Day 27 -> Dictionaries method 

ep1= {12: 56, 14: 78, 18:89, 32: 98  }
ep2={20: 89, 22:99, 24:87}


#update 
ep1.update(ep2)
print(ep1)                                      # Output:{12: 56, 14: 78, 18: 89, 32: 98, 20: 89, 22: 99, 24: 87}


#Removing items
ep1.clear()                  
print(ep1)                                     # Output:{}


#Pop -Remove single value
ep2.pop(20)
print(ep2)                                     # Output:{22: 99, 24: 87}

#Popitem _ Remove last value
ep2.popitem()
print(ep2)                                     # Output:{22: 99}


#del

ep1= {12: 56, 14: 78, 18:89, 32: 98  }
# del ep1  it will create an error , if procceed           
print(ep1)

del ep1[12]
print(ep1)                                      # Output:{14: 78, 18: 89, 32: 98}



