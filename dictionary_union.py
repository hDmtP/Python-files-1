
# a = {1: 'one', 2:'two'}
# b = ((i, i**2) for i in range(3))
# a |= b
# print(a)    ----> What the hell! This code is not working

a={'a','b','c','e'}
b={'e','f'}
x={'c', 'd', 'x', '1', '85','f'}
y={'h','d','m','t','p'}
c=a.union(b)
d=a.union(b,x)
e=a.intersection(b)
f=b.intersection(x)
g=a.symmetric_difference(b)
# h=x.intersection_update(y)
print(c)
print(d)
print(e)
print(f)
print(g)
# print(h)