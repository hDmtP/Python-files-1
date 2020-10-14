from bs4 import BeautifulSoup
import requests

urls=[]

def scrape(site):
   r=requests.get(site)
   s=BeautifulSoup(r.text, 'html.parser')

   for i in s.find_all("a"):
    hrefx = i.attrs['href']
    if hrefx.startswith("https://"):
        site=site+hrefx
        if site not in urls:
            urls.append(site)
            print(site)
            # scrape(site)

if __name__ == "__main__":
    site = str(input("Enter site url:\n"))
    scrape(site)
        
