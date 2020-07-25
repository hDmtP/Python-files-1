''' ***In this source code I learnt that you need to type '==' instead of '=' for not getting an error***  '''




'''
var1 = 23
var2 = 56

var3 = int(input())

if var3>var2:
    print("Greater")
if var3==var2:
    print("Equal")    
else:
    print("Lesser")    
    '''
'''
      #THIS IS LOGICALLY CORRECT


# aGe  =  int(input("Enter Your age\n\n"))   

# if aGe<18:
#     print("You cannot drive a car")
# if aGe>18:
#     print("You can drive a car")    
# else:
#     print("You need License")


         #THIS IS LOGICALLY WRONG


# aGe  =  int(input("Enter Your age\n\n"))   

# if aGe>18:
#     print("You can drive a car")    
# if aGe<18:             
#     print("You cannot drive a car")       #THIS IS LOGICALLY WRONG
# else:
#     print("You need License")


    #THIS IS LOGICALLY CORRECT

# aGe  =  int(input("Enter Your age\n\n"))   

# if aGe>18:
#     print("You can drive a car")    
# if aGe<18:             
#     print("You cannot drive a car")       
# if aGe==18:
#     print("You need License")


   #THIS IS LOGICALLY CORRECT AND IT ALSO REPEATS THE QS FOR INFINITE TIMES

# while True:
#     aGe  =  int(input("Enter Your age\n\n"))   

#     if aGe>18:
#         print("You can drive a car")    
#     if aGe<18:             
#         print("You cannot drive a car")       
#     if aGe==18:
#         print("You need License")



    #LOGICALLY CORRECT AND REPEATS THE LOOP FOR A CERTAIN NUMBER(here for 5 times) OF TIMES.

# for aGe in range(1,6):
#     # while True:
#         aGe  =  int(input("Enter Your age\n\n"))   

#         if aGe>18:
#             print("You can drive a car")    
#         if aGe<18:             
#             print("You cannot drive a car")       
#         if aGe==18:
#             print("You need License")



         #COMPLETELY MESSED UP

# for aGe in range(1,6):
#         aGe  =  int(input("Enter Your age\n\n"))   
    
#         if aGe<18, aGe>60:             
#             print("You cannot drive a car")       
#         if aGe==18:
#             print("You need License")
#         if aGe>18 and aGe<60:
#             print("You can drive a car")    


            
            
            #TRIED.IT WORKED BUT HAD TO CHANGE THE STRATEGY

# aGe = int(input("Enter Your Age\n"))      
# if aGe>=18 and aGe<60:
#     print("You can drive a car")

# else:
#     print("You can't drive a car")    



      #IF WORKED EXACTLY THE WAY I THOUGHT BUT IT HAS BEEN DONE WITHOUT FOR LOOP

# aGe = int(input("Enter Your Age\n"))      
# if aGe>18 and aGe<60:
#     print("You can drive a car")
# elif aGe==18:
#     print("You need practice")
# else:
#     print("You can't dirve a car")    


        #IT HAS BEEN DONE EXACTLY BUT IT CAN BE MORE ADVANCED. IT IS ACTUALLY POSSIBLE BY MY LIMITED KNOWLEDGE BUT IT WILL MAKE MY CODE HEAVY:((

# for aGe in range(1,6):
#     aGe = int(input("Enter Your Age\n"))      
#     if aGe>18 and aGe<60:
#         print("You can drive a car")
#     elif aGe==18:
#         print("You need practice")
#     else:
#         print("You can't dirve a car")    


#HERE IS A VERY GOOD CODE SAMPLE. CREDITS GOES TO Tulshi SHARMA (https://www.youtube.com/channel/UCv7HHAVzGGtzNCFNhEEkrwA).I MODIFIED IT A BIT.

#prototype1
# for age in range(1,6):
#     age=int(input("Enter your age:\n"))
#     if(age>18 and age<70):
#         print("You can drive a car")
#     elif(age<18 and age>6):
#         print("You cannot drive a car")
#     elif(age==18):
#         print("You need to do physical test")
#     else:
#         print("Your present age is not approiate for Driving")


#prototype2
for age in range(1,6):
    age=int(input("Enter your age:\n"))
    if(age>18 and age<70):
        print("You can drive a car")
    elif(age<18 and age>6):
        print("You cannot drive a car")
    elif(age==18):
        print("You need to do physical test")
    elif(age<=6):
        print("You have to wait for it ,Kid")
    elif(age>=70):
        print("Sorry Sir! You are a senior citizen. So you need to take care about your Health.")

'''




        
           
