# Day 53 ->  Class Methods as alternative constructor


class employee:
    def __init__(self, name, age):
        self.name= name 
        self.age= age

    @classmethod              #it is working as an alternative constructor for different type of data type
    def fromstr(cls, str):
        return cls(str.split(" ")[0], int(str.split(" ")[1]))


    
e2= employee("Saboor", 30000)
print(e2.name)
print(e2.age)

str2 = "Tehreem 5000000"
e= employee.fromstr(str2)
print(e.name)
print(e.age)

