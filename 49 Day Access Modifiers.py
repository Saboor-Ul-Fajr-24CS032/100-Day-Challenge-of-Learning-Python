# Day 49 -> Access Modifiers 


class employee:
    def __init__(self):
        self.name="Saboor32"

#Public
a= employee()
print(a.name)


#private
class employee1:
    def __init__(self):
        self.__name="Saboor24CS032"  #Private Attiribute

b= employee1()
#print(b.__name)   can't accessed 
print(b._employee1__name)


#protected
class employee2:
    def __init__(self):
        self._name="Saboor"
    def _fun(self):
        print("this is the fun named function")

class employee3(employee2):
    pass

obj2= employee2()
obj1= employee3()
print(obj1._name)
print(obj2._fun())