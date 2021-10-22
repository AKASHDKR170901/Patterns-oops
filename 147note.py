import re
s=input('Enter pattern to check:')
m=re.search(s,'abaababa')
if m!=None:
    print('Match is available')
    print('Start index:{}and end index:{}'.format(m.start(),m.end()))
else:
    print('Full string not matched')
