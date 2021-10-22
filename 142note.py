import re
matcher=re.finditer('[^a-z]','a7b@k9z')
for m in matcher:
    print(m.start(),'.....',m.group())