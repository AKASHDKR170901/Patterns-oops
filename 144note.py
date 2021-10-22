import re
matcher=re.finditer('a+','abbaaabba')
for m in matcher:
    print(m.start(),'....',m.group())