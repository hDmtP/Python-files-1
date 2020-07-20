
import webbrowser

url = ""
download = url[:12] + "ss" + url[12:]
webbrowser.open(download)

'''
import pyshorteners as ps
url = "https://www.atlassian.com/software/jira?utm_source=quora&utm_medium=paid-social&utm_campaign=P:jira-software|O:ppm|V:quora|G:in|L:en|F:aware&utm_content=P:jira-software|O:ppm|V:quora|G:in|L:en|F:aware|T:interest|Z:topics|A:alla|D:desktop|U:coding_customer-2-freetrial-image"
u = ps.Shortener().tinyurl.short(url)
print(u)
'''
'''
import pyshorteners as ps
url = "https://www.instagram.com/p/CCyHGMDA5MF/"
print(ps.Shortener().tinyurl.short(url))
'''