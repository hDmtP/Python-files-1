# pattern printing
# input = int n
# boolean = true or False
'''
True=
*
* *
* * * 
* * * *
False=
* * * *
* * *
* * 
* 
'''

import time
m = int(input("How many star patterns do you want to make?: "))
for k in range(0, m):
    n = int(input("What should be the maximum numbers of rows in your stAr pattern should be??: "))
    sWitch = int(input("Upward or Downward pattern?(1/0): "))
    sWbool = bool(sWitch)
        
    init=time.time()
    if sWbool==True:
            
        for i in range(1, n+1):
            for j in range(1, i+1):
                print("*", end=" ")
            print()
    elif sWbool==False:
        
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print("*", end=" ")
            print()

    print(f"Total operation time = {time.time()-init}s")

