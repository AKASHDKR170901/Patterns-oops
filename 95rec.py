word=input("Enter word:")
vowels={'a','e','i','o','u'}
d={}
for x in word:
    for x in vowels:
        d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
    print("{} occured {} times".format(k,v))

