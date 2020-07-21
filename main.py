# print('hello world\n')

#INDENTATION
# var:
#(-------------------------------this line is under the above written variable-----------------------------------------------------)


# import math
# print(math.gcd(896,456))


# print(5+9)


# This is a comment
# This is also a comment
'''
This is a multi line comment

'''


# a = 34        #integer
# b= "hDmtP"    #string 
# c = 45.156    #float
# d = 2
# print (a+d)
# print (a-d)  OPERATORS
# print (a*d)
# print (a/d)



# dhara project = 89 -> This is a wrong syntax
#1. variable should start with a letter or underscore
#2. variable cannot start with a number
#3. It can only contain alpha-numeric characters
#4. Variable names are case sensitive: 'Dhara' and 'dhara' are two diferent variables




# typeA = type(a)
# print(typeA)

# typeB = type(b)
# print(typeB)

# typeC = type(c)
# print(typeC)


# variable1 = 31 -->[this variable contains an integer]
# variable2 = "31" -->[this variable contains a string]

#you can put more than one input in a single variable & only the last input will be taken into consideration

# e = 17
# e = "85"            #the last written input of a centain variable will be taken into priority
# print(e)
# print(e+3.2) -->[this code will give an error cauze here e ="85 is taken into consideration as it is written in the last"]


#TYPECASTING
# d = "69"
# print(d+2) will give an error
# d = int(69)
# d = int(d)
# d = float(d)
# d = int(70)
# print(d*8)



#STRINGS
# name = "Dhara"
# print(name)
# name = "Dhara
#               sakt launda hai" ---> This will give an error
# name = ''' Dhara
#                   ek sakt launda hai'''
# print(name)           
# name = 'Dhara'
# print(name[0])
# print(name[3])
# print(name[0:2]) #--->Dh
# print(name[3:4]) #--->r
# print(name[2:7])
# name = '   Dhara  '
# print(name.strip()) #strip fn is used to delete all the spaces
# print(len(name)) #this will include all the spaces as well
# var = name.lower()
# var = name.upper() #you can put more than one input in a single variable & only the last input will be taken into consideration
# var = name.replace('a','x')
# var = name.replace('ara','tam')
# print(var)

# name = "Dhara, Sengupta, Kumar"
# var = name.replace(",","")
# var = name.replace(",","\n")   #--> with space
# var = name.replace(", ","\n")  #--> without space
# print(var)

# stri = " This is a"
# stri1 = " family"
# print(stri + stri1)
# print(name + stri + stri1)
# name1 = "Dhara"
# name2 = "Khan"
# # template = "This is {} and he is a good person named {}".format(name1, name2)
# # template = "This is {0} and he is a good person named {1}".format(name1, name2)
# # template = "This is {1} and he is a good person named {0}".format(name1, name2)
# temp = f"This is {name1} and he is a good person named {name2}" 
# print(temp)

#OPERATORS
# print(78//9)  division operator
#print(78%8)   #modulo operator
# print(45**3)  exponential operator


'''
Python Collections:
1. Lists
2. Tuple
3. Sets
4. Dictionary

'''

#LIST
# lst = [69,79,8,4,5,123]
# # print(lst)
# # var = type(lst)
# # var = lst[0]
# # var = lst[1:5]
# # var = lst[1:5:3]
# # print(var)
# lst[5] = 786
# # print(lst)
# # var = len(lst)
# # lst.append(461) #the 'append' fn will add the element to the mentioned list
# # print(lst)
# # lst.insert(3,461) #here '3' is the index number
# # lst.remove(69)
# # lst.pop()    #--> to remove the last element from a list 
# # del lst[1] # you have to put an index number in the bracket
# # var = lst
# lst.clear()
# var = lst
# print(var)    -----> find more sources from internet 


#TUPLE
#it cannot be changed but TypeCasting is allowed
# a = ("hp", "lenovo", "asus")
# a = list(a)
# var = type(a)
# # print(a)
# print(var)      -----> find more sources from internet  



#SET
# if you don't want to repeat the elements, then use Set
# s1 = {1,2,3,4,5,6,1,3,1,5,6,4}
# s1.add(6856)
# s1.update([45, 689 , 89, 789, 452])
# s1.remove(6856)
# #s1.remove(8520) --> this will give an error as element'8520' is'nt in the set
# s1.discard(8520) #---> but this will not give an error
# # .pop, .del, .clear, .union, .intersection
# print(s1)
# print(len(s1))



# DICTIONARY
# dhDict = {
#     "Name" : "Dhara",
#     "Class" : "6th",
#     "Marks" : 27.88,
#     "Attendence" : 172

# }
# print(dhDict["Marks"])
# dhDict["Marks"] = 80.12
# dhDict.pop("Marks")
# print(dhDict)
# .del, .clear, .pop, .update

# Conditional Statements
# age = input('Enter your Age\n')
# age = int(age)
# if(age>18):
#     print('You Can Drive a Car')
# elif(age==18):
#     print('You are an awesome teen')    
# else:
#      print('You cannot drive')      #HAVE TO DO IN TERMINAL!!



#LOOPS
# for i in range(0, 1000):
#     print(i)       #this will give you a print upto 999

# for i in range(21000, 67000):
#     print(i)


# lst = [435, 7, "dhara"]    
# for item in lst:
#     print(item)
# Use 'for' loop to iterate dictionary, sets and tuples


# i = 0
# while(i<25):
#     i = i+1
#     print(i)   


# i = 0
# while(i<100):
#     i = i+1
#     if i == 69:
#         continue
#     print(i+1)


#DEFINATION

# def greet():
#     print("Good Morning Sir")
#     print("Good Morning Madam")
#     print("Good Morning Uncle")

# greet()    
# greet()

# def sum(a, b):          
#     c = a+b
#     return c

# n = sum(5689, 45876)  
# print(n)  

# def sum(g, h):
#     # print("Here is your Answer: ")
#     i = g + h
#     return i

# w = sum(6995959, 659.01449)  
# print(type(w))   




# def divission(a, b):
#     print('Here is your Answer')
#     c = a//b
#     return c

# n = divission(568978, 45876)  
# print(n)  

    

# OBJECT ORIENTED PROGRAMMING(oop)

# class Employee:
#     def _init_(self, gname, gsalary):    #---> constructor
#         self.name = gname 
#         self.salary = gsalary

# dhara = Employee("dhara", 78)
# print(dhara.name)
# print(dhara.salary) #--------> GOD KNOWS WHY THE CODE IS'NT WORKING


# class Pritam:
#     def _init_(self, age, height):
#         self.age = age
#         self.height = height

# dhara = Pritam("17", "5.11")    
# print(dhara.age)    


