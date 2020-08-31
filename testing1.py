import os
import random
import sys
import re
import math

def compareTriplets(a, b):
    # alice = [a[0], a[1], a[2]]
    # bob = [b[0], b[1], b[2]]
    score = [0, 0]
    for i in range(len(a)):
        if a[i]>b[i]:
            score[0]+=1
        elif a[i]<b[i]:
            score[1]+=1
        
    return score

if __name__ == "__main__":
    # fptr = open(os.environ['_Path'], 'w')
    print("Howdy!")
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a,b)
    print(result)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write("\n")

    # fptr.close()