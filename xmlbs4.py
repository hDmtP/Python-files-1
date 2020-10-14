import urllib2
from bs4 import BeautifulSoup  
url=urllib2.urlopen("http://store.explorelabs.com/index.php?main_page=products_all")  
soup=BeautifulSoup(url,"xml")  
data=soup.find_all(colspan="2")