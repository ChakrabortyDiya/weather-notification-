import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

#creating object
n=ToastNotifier()

def getdata(url):
     r = requests.get(url)  
     return r.text 

htmldata=getdata("https://weather.com/en-IN/weather/today/l/2f30240cc3e91903cecd01d370a0637719b8dcfbafa22e8fb6ba10254d290812")
soup = BeautifulSoup(htmldata, 'html.parser')

current_temp = soup.find_all("span", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY") 

chances_rain = soup.find_all("div", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf") 

temp = (str(current_temp)) 
temp_rain = str(chances_rain) 

result = "current_temp " + temp[128:-9] + "  in Kolkata West Bengal" + "\n" + temp_rain[131:-14]

n.show_toast("live Weather update", result, duration = 60) 