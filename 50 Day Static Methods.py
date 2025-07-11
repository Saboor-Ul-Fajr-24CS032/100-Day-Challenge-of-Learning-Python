# Day 50 -> Static Methods


class numbers:
    def __init__(self, num):
        self.num=num

    def addtonum(self,n):
        self.num = self.num+n
        return self.num

    @staticmethod
    def add(a,b):
        return a+b


a= numbers(10)
print(a.num)
print(a.addtonum(6))
#print(numbers.addtonum(7))   Gives an error
print(a.num)
print(a.add(7,5))
print(numbers.add(7,10))