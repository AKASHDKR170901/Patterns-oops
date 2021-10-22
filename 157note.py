import re,urllib
import urllib.request
u=urllib.request.urlopen("http://www.redbus.in/info/contactus")
text=u.read()
numbers=re.findall('[0-9]{3,4}[- ][0-9-]+',str(text))
for n in numbers:
    print(n)
