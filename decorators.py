
def obj1(func):
    def inner(*args, **kwargs):
        print("/"*30)
        func(*args, **kwargs)
        print("/"*30)
    return inner

def obj2(func):
    def inner(*args, **kwargs):
        print("\\"*30)
        func(*args, **kwargs)
        print("\\"*30)
    return inner
    

@obj1
@obj2
def obj3(arg):
    print(arg)


obj3("Call of Duty")
#---------------------------------------------------------
import inspect

def smart_work(func):
    def inner(*args):
        print("This computational work involves",
        len(args),
        "number of arguments that are"
        )
        return func(*args)
    return inner

@smart_work
def pythagoras(a,b,c):
    if (c**2 == a**2 + b**2):
        print("OK")
    else:
        print("Whoops!")
# print("Done")

    
pythagoras(4,3,5)
print(inspect.signature(pythagoras))
print(inspect.getfullargspec(pythagoras))