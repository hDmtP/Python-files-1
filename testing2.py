import os
import random
import sys
import re
import math

def diagonalDiff(matrix):
    d1=sum(matrix[i][i] for i in range(n))
    d2 =sum(matrix[i][n-1-i] for i in range(n))
    score = abs(d1 - d2)
    return score
    
if __name__ == "__main__":
    # fptr = open(os.environ['_Path'], 'w')
    print("Howdy!")
    n= int(input().strip())
    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = diagonalDiff(matrix)
    print(result)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write("\n")

    # fptr.close()