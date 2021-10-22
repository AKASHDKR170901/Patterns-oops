import re
count=0
matcher=re.finditer('ab','aababaababba')
for m in matcher:
    count=count+1
    print('start:{},end={},group={}'.format(m.start(),m.end(),m.group()))
print('No of occurences:',count)