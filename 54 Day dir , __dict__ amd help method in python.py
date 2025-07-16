# Day 54 -> dir , __dict__ amd help method in python

 

var1= (0,1,2,3,4)
print(dir(var1))


# __dict__ attribute (the values that i set from constructor would e answer)

class person:    
    def __init__(self, name, occu):
        self.name= name 
        self.occu= occu

a=person("Saboor", "learner")
print(a.__dict__)


#help() method
help(person)                       #use in python shell
