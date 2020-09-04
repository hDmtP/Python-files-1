'''
a= 8           # Global variable         
b= 56         # Global variable
c=466              # Global variable

def func1(n):
    print(n, "Howdy!")
    global a
    a=54 + a           # local/private variable
    b=5**2
    print(a, b)
    # print(a, b, a*b, b/a, b%a)
    print(c)

func1("here is me hDmtP")
print(a, b, a*b, b/a, b%a)
'''


x=240
def dhara():
    x=256
    def bnjee():
        global x
        x = 512

    bnjee()
    print("after calling bnjee", x)
print(x)
dhara()
print(x)
