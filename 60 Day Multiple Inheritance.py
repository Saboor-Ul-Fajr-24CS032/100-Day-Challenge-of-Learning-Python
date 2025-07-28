# Day 60 -> Multiple Inheritance 


class parentclass1:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name} ")

class parentclass2:
    def __init__(self, name2):
         self.name2= name2
    def show(self):
        print(f"The name is {self.name2} ")

class parentclass3:
    def __init__(self, name3):
        self.name3= name3
    def show(self):
        print(f"The name is {self.name3} ")


class childclass(parentclass1,parentclass2, parentclass3):
    def __init__(self, name, name2, name3):
        self.name= name
        self.name2= name2
        self.name3= name3
    
c= childclass("firstname", "secondname", "thirdname")
print(c.name)
print(c.name2)
print(c.name3)
c.show()                                                   #When using the same name methods it will count the first class in child multi class
print(childclass.mro())