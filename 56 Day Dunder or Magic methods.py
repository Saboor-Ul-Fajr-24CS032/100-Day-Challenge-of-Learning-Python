# Day 56 -> Dunder or Magic methods



class employee:
    name= "Saboor"
    def __len__(self):
        a=0
        for b in self.name:
            a= a+1
        return a
    
    def __str__(self):
        return f"The name of the person is {self.name}  str"
    
    def __repr__(self):
        return f"The name of the person is {self.name}  repr"
    
    def __call__(self):
        return f"Saboor name is used today"

e= employee()
print(e)
print(e.name)
print(len(e))
e()