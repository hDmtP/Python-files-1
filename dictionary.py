'''
d1 = {}
print(type(d1))                                                                   #()-->tuple
                                                                                  #{}-->dictionary
                                                                                  #[]-->list
                                                                                   
d2 = {"Dhara":{"B":"tea+roti", "L":"rice", "S":"biscutes+milk", "D":"Roti"}, "Poly":"chowmin", "Goutam":"bidie"}
d2["Laptop"] = "current"
d2[19] = "charge"

del d2[19]

d3 = d2.copy()
del d3['Poly']

print(d3)




print(d2)
print(d2['Poly'])
print(d2['Goutam'])

print(d2['Dhara'])
print(d2.get("Dhara"))
print(d2['Dhara']['B'])


d2.update({"Cat":"fish"})
print(d2)

print(d2.keys())
print(d2.items())
'''



    
print("Welcome to Dictionary")
D1={"abase":" cause to feel shame", "benefit":"advantage", "callow":"young and inexperienced", "dally":"waste time", "endear":"make attractive"}
print("Please enter your word: ")
Search=input()
if Search in D1:
    print(D1[Search])
    print("Thanks for using Dictionary")
else:
    print("Sorry! word", Search, "is not available in D1")    
