import re
s=input("Enter no:")
m=re.fullmatch('(0|91)?[6789]\d{9}',s)
if m!=None:
    print("Valid")
else:
    print('Invalid')
