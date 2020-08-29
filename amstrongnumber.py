'''
print("enter any integer:\n")
n=int(input())

count=0
while(n>0):
    count+=1
    n=n//10


temp = n 
sum=0
while(temp>0):
    digit=temp%10
    sum+=digit**3
    temp=temp//10
if(n==sum):
    print(n, " is an Amstrong Number\n")    
else:
    print(n," is NOT an Amstrong Number\n")      
'''

                                      #//-------||-------\\#


n = int(input("Enter any int value of n: "))  
count=0
m=n
while(m>0):
    count+=1
    m=m//10            

sum=0
temp=n


while(temp>0):
    digit=temp%10
    sum+=digit**count
    temp=temp//10
if(n==sum):
    print(n, "is an Amstrong Number\n")    
else:
    print(n,"is NOT an Amstrong Number\n")  

