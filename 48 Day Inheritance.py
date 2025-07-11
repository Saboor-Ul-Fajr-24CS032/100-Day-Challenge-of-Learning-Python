# Day 48 -> Inheritance



class employee:
    def __init__(self, name , ID):
        self.name= name
        self.ID = ID

    def ShowDetails(self):
        print(f"The name of the employee is {self.name} and ID is {self.ID}")
        


class programmer(employee):
    def showlanguage(self):
        print("The default language is python ")


var1 = employee("Saboor", "24CS032")
var1.ShowDetails()

var2= programmer("Tehreem",18)
var2.ShowDetails()
var2.showlanguage()