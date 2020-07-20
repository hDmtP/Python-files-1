
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=r'C:\Users\user\Downloads\covid19.ico',
        timeout=12
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == "__main__":
     while True:
    #  notifyMe("Dhara", "Let's stop the spread of corona virus together")
        myHtmlData = getData('https://www.mohfw.gov.in/')
        # print(myHtmlData)

        soup = BeautifulSoup(myHtmlData, 'html.parser')
    #  print(soup.prettify())
        myDatastr = ""

        for tr in soup.find_all('tbody')[0].find_all('tr'):
               myDatastr += tr.get_text()
               myDatastr = myDatastr[0:]
               itemList = myDatastr.split("\n\n")
               states = ['West Bengal']
               for item in itemList[0:35]:
                  dataList = item.split('\n')
if dataList[1] in states:
        #  print(dataList)
    nTitle = "Cases of Covid-19"
    nText = f"STATE: {dataList[1]}\nCases {dataList[2]}\nCu+Dis+Mi {dataList[3]}\nDeaths {dataList[4]}"
    notifyMe(nTitle, nText)
    time.sleep(3600)
       
    
