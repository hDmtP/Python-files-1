from bs4 import BeautifulSoup
import requests

url = "https://instagram.com/{}/"

def parse_data(s):
    data={}
    s=s.split("-")[0]
    s=s.split(" ")

    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
    return data

def scrape(username):
    r=requests.get(url.format(username))
    s=BeautifulSoup(r.text, "html.parser")
    meta=s.find("meta", property="og:description")
    return parse_data(meta.attrs['content'])

if __name__ == "__main__":
    username=str(input("Enter username :\n"))
    data = scrape(username)
    print(data)
    
    