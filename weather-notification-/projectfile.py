import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n=ToastNotifier()
def getdata(url):
     r = requests.get(url)  
    return r.text # type: ignore
htmldata=getdata("https://weather.com/en-IN/weather/today/l/c2c95ea60f4ef581b88c5c173d2ef178276d8fc26e6b39ad66f2e2e01f933c37")
