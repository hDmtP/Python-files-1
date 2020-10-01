import whois
liNk = str(input("Enter the site url: \n"))
domain = whois.whois(liNk) 
print(domain.__dict__)    