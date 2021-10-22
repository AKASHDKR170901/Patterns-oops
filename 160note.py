import re
s=input('Enter car no:')
m=re.fullmatch('TN[A-Z]{2}\d{4}',s)
if m!=None:
    print('Valid')
else:
    print('Invalid')
