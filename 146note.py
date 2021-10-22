import re
s=input('Enter pattern to check:')
m=re.fullmatch(s,'abcdefgh')
if m!=None:
    print('Full string macthed')
else:
    print('full string not matched')


