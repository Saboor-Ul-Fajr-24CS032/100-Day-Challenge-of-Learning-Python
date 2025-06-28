# Day 41 -> lambda Function 



multipleby4= lambda x: x*4
sum = lambda a, b, c, d ,e: a+b+c+d+e 

print(multipleby4(10))
print(sum(2,3,4,5,6))


def apply(fx, value):
    return 10+ fx(value)

print(apply(multipleby4, 4))
print(apply(lambda x: x*4, 4))