# Day 46 -> Decorators in python


def greet(fx):
    def mfx(*args, **kwargs):
        print("Hey , Saboor decorate your function")
        fx(*args, **kwargs)
        print("Thank you for asking me to help")
    return mfx


@greet
def hello():
    print("Hello, I am doing programs")

hello()
#greet(hello)()

@greet
def add(a,b):
    print("the addition is ",  a+b)

add(3,4)




