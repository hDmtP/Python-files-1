import re
str1="hello! this is an automated pyton generated email from zotacgtxgbvram@gmail.com, hdmtp466@hdmtp645.com"
list1=re.findall(r'\w+@\S+\w',str1)

op=open("email_store.txt","a")

j=0
for i in list1:
    j+=1
    op.write(f"Email({j}):{i}\n")
op.close()
print(f"Email's are:{list1}")
print(f"Total Email's are:{j}")