# Day 47 -> Getters and Setters in python


class Aclass:
    def __init__(self, value):
        self.value1=value

    def show(self):
        print(f"The value of variable is {self.value1}")
    
    #getter
    @property
    def ten_value(self):
        return 10*self.value1
    
    #setter
    @ten_value.setter
    def ten_value(self, new_value):
        self.value1= new_value/10
        

obj= Aclass(15)

obj.ten_value=100
print(obj.ten_value)


obj.show()