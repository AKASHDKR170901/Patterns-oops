word=input("Enter words:")
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)
print(sorted(d))
for k,v in sorted(d.items()):
    print("{} occured {} times".format(k,v))
