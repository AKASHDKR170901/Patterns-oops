import re
matcher=re.finditer('\d','a7b6k9z')
for m in matcher:
   print(m.start(),m.end(),m.group())
