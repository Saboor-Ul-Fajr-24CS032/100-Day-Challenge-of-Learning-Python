#Day 8-> String Slicing and Operation of String


var = "Python"
print(var[0])                       # Output: P
print(var[3])                       # Output: h


# word(lengthofword -1)
print(var[-3])                      # Output:h


var1 = "Coding"
print(len(var1))                      # Output: 6


#string slicing [start:end]
var2 = "Programming"
print(var2[0:5])                      # Output: Progr
print(var2[3:8])                      # Output: gram
print(var2[:7])                       # Output: Program  (from start to index 6)
print(var2[5:])                       # Output: amming   (from index 5 to end)


#Complete slicing 
var3 = "Python"
print(var3[::2])                      # Output: Pto (every 2nd character is showing)
print(var3[::-1])                     # Output: nohtyP (reverses the string)
