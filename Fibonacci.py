import time

def fiboIter(n):
   prevNum=0
   currentNum=1
   for i in range(1, n):
       preprevNum=prevNum
       prevNum=currentNum
       currentNum=preprevNum+prevNum
   return currentNum   

def fiboRecur(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return  fiboRecur(n-1)+fiboRecur(n-2)

if __name__ == "__main__":
    num=int(input("Enter a number: ")) 
    init=time.time()

    print(f"recursion value of fib({num}) is {fiboRecur(num)}")       
    print(f"iterative(less pressure on cpu) value of fib({num}) is {fiboIter(num)}")  
    print((f"It took ({time.time()-init}) seconds to complete the operation"))     
