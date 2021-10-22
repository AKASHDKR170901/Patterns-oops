import re
matcher=re.finditer('\w','a7b6@k8z')
for m in matcher:
    print(m.start(),'.....',m.group())
