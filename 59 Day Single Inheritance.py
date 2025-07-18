# Day 59 -> Single Inheritance

class parentclass:
    def __init__(self, name, parentobj):
        self.name= name
        self.parentobj= parentobj

    def samemethod(self):
        print("I am from parent method ")
    
class childclass(parentclass):
    def __init__(self, name , childobj):
        parentclass.__init__(self, name, parentobj="parentword" )
        self.childobj= childobj

    def samemethod(self):
        print("i am from child class")



c = childclass("childclass", "child word using obj")
c.samemethod()

p= parentclass("parentclass", "parent word using obj")
p.samemethod()



