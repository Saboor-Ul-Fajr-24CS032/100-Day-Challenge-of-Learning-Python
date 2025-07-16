# Day 55 -> Super Keyword


class parent:
    def __init__(self, name1, name2):
        self.name1=name1
        self.name=name2
    def Parentmethod(self):
        print("This is parent method")

class child(parent):
    def __init__(self, name1, name2, name3):
        super().__init__(name1,name2)
        self.name3= name3
        
    def childmethod(self):
        print("this is child method")
        super().Parentmethod()
        print("parent method is also called")


objchild= child("mama","papa", "child")
objchild.childmethod()
objchild.Parentmethod()
print(objchild.name1)