# Day 62 -> Hybrid and Hierarchical Inheritance



#Hybrid Inheritance (Combination of multilevel and multiple )

class baseclass:
    pass

class derivedclass1(baseclass):
    pass

class derivedclass2(baseclass):
    pass

class derivedclass3(derivedclass1, derivedclass2):
    pass 


#Hierarchical Inheritance (A Tree like structure)

class baseclass2:
    pass

class d1(baseclass2):
    pass

class d2(baseclass2):
    pass

class d3(d1):
    pass