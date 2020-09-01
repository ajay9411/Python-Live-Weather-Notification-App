import requests 
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()

def getdata(url):
    r = requests.get(url) 
    return r.text


# get link from https://weather.com for your city
htmldata = getdata("https://weather.com/en-IN/weather/today/l/619ae1792402fd295f376593549c861b5493a82d6d0fce7d4cf49605f6cbaf8a")

soup = BeautifulSoup(htmldata,'html.parser') 

current_temp = soup.find_all("span", class_="_-_-node_modules--wxu-components-src-organism-CurrentConditions-CurrentConditions--tempValue--3KcTQ")

current_feel = soup.find_all("div", class_="_-_-node_modules--wxu-components-src-organism-CurrentConditions-CurrentConditions--phraseValue--2xXSr")

chances_rain = soup.find_all("div", class_="_-_-node_modules--wxu-components-src-organism-CurrentConditions-CurrentConditions--precipValue--RBVJT")

temp = (str(current_temp)) 
feel=(str(current_feel)) 
rain = str(chances_rain)

# print(temp[146:-8])
# print(feel[139:-7])
# print(rain[149:-14])

# set index according to result

result = "Currently "+ temp[146:-8] + " C in Mathura \n"+feel[139:-7]+"\nAnd " + rain[149:-14]

n.show_toast("Live Weather update", result, duration = 15)