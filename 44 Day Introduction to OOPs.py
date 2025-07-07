#  Day 44 -> Introduction to OOPs


class person:
    name = "saboor"
    Status= "student"
    networth= 100
    def personalinfo(self):                               #self means the object for which the method is called 
        print(f'{self.name} is a {self.Status}')


a= person()
a.name="Saboor-Ul-Fajr"
a.networth= 50
a.Status='learner'
print(a.name,a.networth)
a.personalinfo()


b= person()
b.name= "tehreem"
b.networth=10000000
b.personalinfo()
