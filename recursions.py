import time
def factorial_recur(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial_recur(n-1)

def factorial_iter(n):
    fac = 1
    for i in range(1, n+1):
        fac = fac*i
    return fac
        

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n==3:
        return 3
    else:
        return fibonacci(n-1) + fibonacci(n-2)




if __name__ == "__main__":
    
    
    init=time.time()

    # print(factorial_recur(value))
    # print(factorial_iter(value))
    print(fibonacci(value))
    print(f"Operation time = {time.time() - init}s")
