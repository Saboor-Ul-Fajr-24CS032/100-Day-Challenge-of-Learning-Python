# Day 45 -> Constructors in python


class person:
    
    def __init__(self, name, occu):
        self.name= name 
        self.occu= occu

    def info(self):
        print(f"{self.name} is a {self.occu}. ")


a=person("Saboor", "learner")
b=person("tehreem", "student")
a.info()
b.info()
