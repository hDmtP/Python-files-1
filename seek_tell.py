q=int(input("Enter the index number: "))
f=open("dhara.txt")
# print(f.tell())
print(f.readline())
print(f.seek(q))

# print(f.tell())
print(f.readline())
print(f.tell())
f.close()

