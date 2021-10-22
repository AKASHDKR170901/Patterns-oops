import re
count=0
pattern=re.compile('ab')
matcher=pattern.finditer('abaaabaa')
for match in matcher:
    count=count+1
    print('Match is available at start index:',match.start())
print('No of occurences:',count)

