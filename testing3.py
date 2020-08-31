if __name__ == "__main__":
    print("Howdy!")
    n= int(input().strip())
    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    print(matrix)