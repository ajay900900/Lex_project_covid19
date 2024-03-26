import sys
from urllib.request import Request, urlopen
webpage=sys.argv[2]
req = Request(webpage,headers ={'User-Agent':'Mozilla/5.0'})
from urllib.request import urlopen

webpage = urlopen(req).read()   
name=sys.argv[1]
 
mydata = webpage.decode("utf8")
f=open(name,'w',encoding="utf-8")
f.write(mydata)
f.close
