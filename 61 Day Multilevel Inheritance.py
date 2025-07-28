# Day 61 -> Multilevel Inheritance


class mainclass:
    def __init__(self):
        pass

class derived1(mainclass):
    def __init__(self):
        super().__init__()
        
class derived2(derived1):
    def __init__(self):
        super().__init__()
        

class animal:
    def __init__(self, name ):
        self.name=name

    def todo(self):
        print("they all can eat ")

class mammal(animal):
    def __init__(self, name, fourlegs):
        animal.__init__(self, name)
        self.fourlegs= fourlegs

    def todo(self):
        animal.todo(self)
        print("They have four legs ")

class cat(mammal):
    def __init__(self, name, fourlegs, domeow):
        mammal.__init__(self , name, fourlegs)
        self.domeow= domeow
    
    def todo(self):
        mammal.todo(self)
        print("It can meow ")



obj= cat ("Billy", True, True)
obj.todo()
print(cat.mro())