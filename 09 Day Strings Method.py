#Day 9 -> Strings Method

var = "Saboor Doing Work"


# Upper
print(var.upper())                                       #SABOOR DOING WORK


# LOwer
print(var.lower())                                       #saboor doing work


#Strip
var1= " hey string ee"
print(var1.strip())                                      #hey string ee


#rstrip
print(var1.rstrip("e"))                                  # hey string


#replace
print(var1.replace("string", "girl"))                    # hey girl ee


#Split
print(var1.split("string"))                              #[' hey ', ' ee']


#Capitalize
var2= "hello"
print(var2.capitalize())                                 #Hello


#center
print(var2.center(15))                                   #     hello

print(var2.center(20, "."))                              #.......hello........


#Count
print(var2.count('l'))                                   #2


#endswith
print(var2.endswith("o"))                                #True

print(var2.endswith("ll", 1, 4))                         #True


#find
var3= "I'm a coder, it is a part of my coding journey."
print(var3.find("is"))                                   #20

print(var3.find("engineer"))                             #-1


#Index 
print(var3.index("is"))                                  #20

#print(var3.index("engineer")) ---> Raises an error



#ialanum
print(var3.isalnum())                                    #False

var4= "hellotoall100"
print(var4.isalnum())                                    #True



#isalpha
print(var4.isalpha())                                     #False

var5="onlyalphabet"
print(var5.isalpha())                                     #True



#islower
print(var5.islower())                                     #True



#isprintable
var6= "listen!\n"
print(var6.isprintable())                                  #False

print(var5.isprintable())                                  #True



#isspace
var7= "hey      "
print(var7.isspace() )                                     #False

var8="              "
print(var8.isspace())                                      #True



#istitle
var9 = "Harmain Public Higher Secondary School" 
print(var9.istitle())                                       #True



#isupper
var10="WHO"
print(var10.isupper())                                      #True



#startswith
print(var9.startswith("Harmain"))                           #True



#swapcase
print(var9.swapcase())                                      #hARMAIN pUBLIC hIGHER sECONDARY sCHOOL



#title
var11= "Learning coding sometimes can be easy. hahahaha"
print(var11.title())                                        #Learning Coding Sometimes Can Be Easy. Hahahaha