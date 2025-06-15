# Day 26 -> Dictionaries

dict1 = {'Name' : "Saboor", "grade ": "A1", "Class": "2nd semester" }
print(dict1)


dict= {"Saboor": "student",
"laptop ": "Device" , 32 : "rollnumber"
}

print(dict["Saboor"])     #will throws an error when item is not available

print(dict.get(32))       #will not throw an error when item is not available , but instead give none


#To excess all keys
print(dict.keys())         #dict_keys(['Saboor', 'laptop ', 32])


#to excess values
print(dict.values())        #dict_values(['student', 'Device', 'rollnumber'])


#To excess values in keys
for i in dict.keys():
    print(dict[i])


#Usinf f string
for var in dict.keys():
    print(f"The value of key {var} is {dict[var]}")


#using items 
print(dict.items())
for key , value in dict.items():
      print(f"The value of key {key} is {value}")