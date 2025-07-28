# Day 68 -> Generators in python


def Generator():
    for i in range(400):
        yield i

gen = Generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# for var in gen :
#     print(var)