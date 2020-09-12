def matrix_mult():
    for i in range(0,len(a)):
        for j in range(0, len(b[0])): 
            for k in range(0,len(b)):
                c[i][j]+=a[i][k]*b[k][j]
                return c

if __name__ == "__main__":
    print("Howdy!welcom to matrix-multiplication. Please print below how many coloumns do you want?")
    n= int(input().strip())
    print("Give space after each element")
    a = []
    b = []
    c = []
    x = 1
    y = 1
    for _ in range(n):
        print("Print the elements in the row No.", x, ". PLease input a constant number of elements in each row")
        a.append(list(map(int, input().rstrip().split())))
        x+=1
    print("a=", a)
    for _ in range(n):
        print("Print the elements in the row No.", y, ". PLease input a constant number of elements in each row")
        b.append(list(map(int, input().rstrip().split())))
        y+=1
    print("b=", b)
    d=b.copy()

    for i in range(n):
        for j in range(len(d[0])):
            d[i][j]=0
            c=d
    print(c)
    result=matrix_mult()
    print(result)


    