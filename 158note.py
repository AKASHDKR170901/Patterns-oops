import re
s=input('Enter mail id:')
m=re.fullmatch('[a-zA-Z0-9]*@gmail.com',s)
if m!=None:
    print('Valid')
else:
    print('Invalid')
#m=re.fullmatch('\w[a-zA-Z0-9_.]@(gmail|rediffmail|yahoo)[.][a-z]+',s)
