#abs => absolute
print(abs(69+69j))

#all => OR gate
'''
mylist = [True, True, True]
x = all(mylist)
print(x)
'''
'''
mylist = [0, 1, 1]
x = all(mylist)
print(x)
# Returns False because 0 is the same as False
'''
'''
mytuple = (0, True, False)
x = all(mytuple)
print(x)
# Returns False because both the first and the third items are False
'''
'''
myset = {0, 1, 0}
x = all(myset)
print(x)
# Returns False because both the first and the third items are False
'''
'''
mydict = {0 : "Apple", 1 : "Orange"}
x = all(mydict)
print(x)
# Returns False because the first key is false.
# For dictionaries the all() function checks the keys, not the values.
'''
'''
mydict = {1 : "Apple", 0 : "Orange"}
x = all(mydict)
print(x)
#returns false ??????!
'''

#any => AND gate

#ascii => returns readable versions of any objects
x = ascii("My name is Ståle. বওইগুলও")
print(x)

#bin => decimal number to binary
print(bin(36))

#bool
print(bool(1))