import re
s=input('Enter mobile no:')
m=re.fullmatch('[6-9]\d{9}',s)
if m!=None:
    print('valid')
else:
    print('Invalid')
    
