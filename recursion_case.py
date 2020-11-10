def listsum(arr):
    print("lol")
    backup = 0
    for i in range(len(arr)):
        # if (len(arr)==0 or len(arr)==1):
        #     if len(arr)==0:
        #         print(0)
        #     else:
        #         print(arr[0])
        # if len(arr)==0:
        #     break
        backup += arr[i]
        arr = arr.remove(arr[i])
    print(backup)

arr = [2,4,6]
print(len(arr))
listsum(arr)