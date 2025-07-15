# Day 51 -> Instance Variable vs Class Variable

class employee:
    companyname="Apple"              #Class variable
    def __init__(self, name):
        self.name = name              #instance variable
        self.raise_amount=0.02

    def showdata(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyname} is {self.raise_amount}")


emp1= employee("Saboor")
#emp1.showdata()
emp1.companyname=  "Google"

employee.showdata(emp1)



emp2= employee("tehrrem")
emp2.raise_amount=0.3

emp2.showdata()

