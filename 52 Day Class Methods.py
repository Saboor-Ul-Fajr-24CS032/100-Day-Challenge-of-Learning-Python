# Day 52 -> Class Methods


class employee:
    company="Google"
    def show (self):
        print(f"The name is {self.name} and the company is {self.company}")



    @classmethod          #to directly make changes in class and it happens like this because the first argument it takse is class not instance
    def changecompanyname(var1, newcompany):
        var1.company= newcompany


e1= employee()
e1.name= "saboor"
e1.show()
e1.changecompanyname("Nestle")
e1.show()
print(e1.company)
print(employee.company)
print(employee.changecompanyname("Harry"))