'''
import urllib3
print(urllib3.urlopen('http://ip.42.pl/raw').read())
'''

'''
import requests
print(requests.get('http://ip.42.pl/raw').text)
'''

import socket
hostn = socket.gethostname()
IPAd = socket.gethostbyname(hostn)
print("YOUR IP ADRESS IS: "+ IPAd)