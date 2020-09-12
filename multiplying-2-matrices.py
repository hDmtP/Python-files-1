a=[[1,5,7],
  [4,0,2],
  [6,0,3]]

b=[[1,0],
  [1,0],
  [5,0]]

c=[[0,0],
  [0,0],
  [0,0]]

for i in range(0,len(a)):
    for j in range(0, len(b[0])): 
        for k in range(0,len(b)):
            c[i][j]+=a[i][k]*b[k][j]

for row in c:
    print(row)