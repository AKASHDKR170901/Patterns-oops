import re
s=input('Ener to validate:')
m=re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',s)
if m!=None:
    print(s,'is valid in yava identifier')
else:
    print(s,'is not valid in yava identifier')
