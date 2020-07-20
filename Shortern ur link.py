import pyshorteners as ps
url = input('Paste link\n')
print("Here is your shorterned link: ")
print(ps.Shortener().tinyurl.short(url))
a = input()