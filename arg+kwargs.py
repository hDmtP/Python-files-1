def myfun(arg1, *argv):
    print("First argument:", arg1)
    for arg in argv:
        print("rest other arguments:", argv)

myfun("time.time", "()", "-", "init")

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s==%s" %(key, value))

myFun(first="Geeks", second="for", third="geeks")

def myfUn(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ("Geeks", "for", "geeks")
myfUn(*args)

kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "geeks"}
myfUn(**kwargs)

def myfuN(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

myfuN('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")
    
