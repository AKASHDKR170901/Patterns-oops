import re,urllib
import urllib.request
sites=['https://www.google.com/','http://rediff.com']
for s in sites:
    print('Searching....',s)
    u=urllib.request.urlopen(s)
    text=u.read()
    title=re.findall('<title>.*</title>',str(text),re.IGNORECASE)
    print(title[0])
