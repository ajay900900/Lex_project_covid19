from urllib.request import Request, urlopen
from urllib.request import  urlopen
req = Request('https://www.worldometers.info/coronavirus/country/india',headers ={'User-Agent':'Mozilla/5.0'})

webpage = urlopen(req).read()
mydata = webpage.decode("utf8")
my_data_={}
f=open('covid19.html','w',encoding="utf-8")
f.write(mydata)
f.close
