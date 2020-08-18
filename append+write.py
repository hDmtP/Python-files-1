'''
d=open('dhara2.txt', 'a')
a=d.write("Pritam Dhara")
print(a)
d.close()
'''
#append ---> a ---> add new content to the file
#write ----> w ---> will rewrite every content in the file

'''
p=open('dhara2.txt', 'r+')
print(p.read())
p.write("+hDmtP")
'''
#read&write ---> r+ ----> to handle read and write both