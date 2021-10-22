import re
s=input("enter pattern to check:")
m=re.match(s,'abcdefgh')
if m!=None:
    print('Match is available at the begining')
    print('start index:{}and end index:{}'.format(m.start(),m.end()))
else:
    print('Match is not available at the begining of the string')


